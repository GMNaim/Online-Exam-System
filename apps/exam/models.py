from django.db import models


class AuditTrail(models.Model):
    hashed_id = models.CharField(null=True, blank=True, max_length=16, unique=True)
    # created_by = models.CharField(max_length=500, blank=True, null=True)
    # updated_by = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Question(AuditTrail):
    question_text = models.TextField()
    option_1 = models.CharField(max_length=255, null=True, blank=True)
    option_2 = models.CharField(max_length=255, null=True, blank=True)
    option_3 = models.CharField(max_length=255, null=True, blank=True)
    option_4 = models.CharField(max_length=255, null=True, blank=True)
    correct_answer = models.CharField(max_length=255)
