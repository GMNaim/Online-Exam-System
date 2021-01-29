from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# ugettext is a unicode version of a translatable string.
# ugettext_lazy is a "lazy" version of that. Lazy strings are
# a Django-ism; they are string-like objects that don't
# actually turn into the real string until the last possible minute.
# Often, you can't know how to translate a string until late in the process.
from apps.core.account.manager import UserManager
from apps.core.base.utils.basics import random_hex_code


class AuditTrail(models.Model):
    hashed_id = models.CharField(null=True, blank=True, max_length=16, unique=True)
    created_by = models.CharField(max_length=500, blank=True, null=True)
    updated_by = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            # Only set created_by during the first save.
            self.created_by = exposed_request.user.id
            self.updated_by = self.created_by
            # For each object a new unique hashed id will be generated.
            # This will be used instead of default id of each model.
            self.hashed_id = random_hex_code(length=16)
        else:
            self.updated_by = exposed_request.user.id
        super(AuditTrail, self).save(*args, **kwargs)


class ActivityLog(AuditTrail):
    store_json = models.TextField(blank=True)
    description = models.CharField(max_length=500)
    ip_address = models.CharField(max_length=50)
    browser_details = models.CharField(max_length=500)

    def __str__(self):
        return self.description


class Resource(AuditTrail):
    name = models.CharField(max_length=50, blank=False)
    icon = models.CharField(max_length=60, blank=True, null=True)
    code = models.CharField(max_length=50, blank=False, null=False, unique=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    parent = models.CharField(max_length=10, blank=True, null=True)
    order_for_sidebar = models.FloatField(default=1111)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'parent')


class Permission(AuditTrail):
    name = models.CharField(max_length=50, blank=False,
                            null=False, unique=True)
    code = models.CharField(max_length=50, blank=False,
                            unique=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='resource_permission')

    def __str__(self):
        return self.name


class Role(AuditTrail):
    name = models.CharField(max_length=50, blank=False,
                            null=False, unique=True)
    code = models.CharField(max_length=50, blank=False, unique=True)
    permission = models.ManyToManyField(Permission, related_name='role_permission')

    def __str__(self):
        return self.name


class User(AbstractUser):
    GENDER = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other')
    )

    middle_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True, null=False, blank=False)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False,
                                validators=[RegexValidator(
                                    regex='[-a-zA-Z0-9_.]{4,50}$',
                                    message='Username contains alphanumeric, underscore and period(.). Length: 4 to 50'
                                )])

    mobile_number = models.CharField(max_length=12, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, default=1)
    address = models.TextField(blank=True, null=True)
    country = models.IntegerField(default=1)
    # activation_url = models.CharField(max_length=500, blank=False, default=get_activation_url)
    profile_picture = models.ImageField(upload_to='user/profile_picture/', blank=True, null=True)
    signature = models.ImageField(upload_to='user/signature/', blank=True, null=True)

    initial = models.BooleanField(null=False, blank=False, default=True)
    need_to_change_password = models.BooleanField(null=False, blank=False, default=False)
    password_updated_at = models.DateTimeField(null=True, blank=True)
    is_locked = models.BooleanField(null=False, blank=False, default=False)
    locked_at = models.DateTimeField(null=True, blank=True)
    unsuccessful_attempt = models.IntegerField(null=False, blank=False, default=0)
    hashed_id = models.CharField(null=True, blank=True, max_length=16, unique=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT,
                             null=False, blank=False,
                             related_name='user_role',
                             default=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.pk:
            self.hashed_id = random_hex_code(length=16)
        super(User, self).save(*args, **kwargs)
