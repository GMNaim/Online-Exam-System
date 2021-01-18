from django.db import models

from apps.core.account.models import AuditTrail


class Question(AuditTrail):
    question_text = models.TextField()
    option_1 = models.CharField(max_length=255, null=True, blank=True)
    option_2 = models.CharField(max_length=255, null=True, blank=True)
    option_3 = models.CharField(max_length=255, null=True, blank=True)
    option_4 = models.CharField(max_length=255, null=True, blank=True)
    correct_answer = models.CharField(max_length=255)
