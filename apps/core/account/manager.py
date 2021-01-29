from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


# ugettext is a unicode version of a translatable string.
# ugettext_lazy is a "lazy" version of that. Lazy strings are
# a Django-ism; they are string-like objects that don't
# actually turn into the real string until the last possible minute.
# Often, you can't know how to translate a string until late in the process.


class UserManager(BaseUserManager):
    # We can optionally serialize managers into migrations and have them
    # available in RunPython operations. This is done by defining a
    # use_in_migrations attribute on the manager class:
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """ Creates and saves a User with the given email and password """
        if not email:
            raise ValueError(_('Email must be needed'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # these user will be normal user
        extra_fields.setdefault('is_superuser',
                                False)  # Insert key with a value of default if key is not in the dictionary.
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        # These user will be superuser with the given email and password
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have 'is_superuser=True'."))

        return self._create_user(email, password, **extra_fields)
