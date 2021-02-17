from django.db import models
from django.utils.text import slugify

from apps.core.account.models import AuditTrail, User


class Course(AuditTrail):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Question(AuditTrail):
    TYPE = ((1, 'Multiple Choice'),
            (2, 'Descriptive'),)

    question_text = models.TextField()
    type = models.IntegerField(choices=TYPE, default=1)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='question_course')
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question_text)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('course', 'slug')

    def __str__(self):
        return self.question_text


class Option(AuditTrail):
    option_text = models.CharField(max_length=255)
    is_correct_option = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.option_text}: {self.question.question_text}"


class Exam(AuditTrail):
    STATUS = ((1, 'Scheduled'),
              (2, 'Running'),
              (3, 'Finished'),)
    title = models.CharField(max_length=100)
    question = models.ManyToManyField(Question, related_name='exam_question')
    slug = models.SlugField(unique=True, null=True, blank=True)
    exam_datetime = models.DateTimeField()
    exam_duration = models.IntegerField(help_text='Time in minute')
    correct_mark = models.FloatField(default=1)
    total_mark = models.FloatField()
    wrong_mark = models.FloatField(default=0)
    exam_status = models.IntegerField(choices=STATUS, default=1)
    exam_code = models.CharField(max_length=50)
    total_questions = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        self.total_questions = Question.objects.filter(exam_question=self.id).count()
        super().save(*args, **kwargs)


class StudentAnswerSheet(AuditTrail):
    """ Student given answer will store here """
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='studentAnswerSheet_student')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='studentAnswerSheet_exam')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='studentAnswerSheet_question')
    student_answer = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField()
    questions_correct_answer = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student.username}-  " \
               f"{self.exam.title}- " \
               f"{self.question.question_text}"


class StudentExamResult(AuditTrail):
    """ Student exam's final result will be store here """
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='studentExamResult_student')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='studentExamResult_exam')
    date_of_student_exam = models.DateTimeField(auto_now_add=True)
    right_answer_count = models.IntegerField()
    wrong_answer_count = models.IntegerField()
    total_marks_count = models.IntegerField()

    def __str__(self):
        return f"{self.student.username}-" \
               f" {self.exam.title} -" \
               f" {self.total_marks_count}"
