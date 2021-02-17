from django.contrib import admin
from .models import Question, Course, Option,Exam, StudentAnswerSheet, StudentExamResult

admin.site.register(Course)
admin.site.register(Option)
admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(StudentAnswerSheet)
admin.site.register(StudentExamResult)
