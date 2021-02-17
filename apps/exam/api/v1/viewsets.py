from rest_framework import viewsets
from apps.exam.models import Course, Question, Option, Exam, StudentAnswerSheet
from apps.exam.api.v1.serializers import CourseSerializer, QuestionSerializer, OptionSerializer, ExamSerializer, StudentAnswerSheetSerializer
from apps.core.account.permission import UserAccessApiBasePermission
from apps.core.account.viewset import CustomViewSet
from apps.core.base.utils.basics import json_parameter_validation


class CourseViewSet(CustomViewSet):
    serializer_class = CourseSerializer
    permission_classes = [UserAccessApiBasePermission]
    model = Course
    queryset = Course.objects.all()
    lookup_field = 'hashed_id'


class QuestionViewSet(CustomViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [UserAccessApiBasePermission]
    model = Question
    queryset = Question.objects.all()
    lookup_field = 'hashed_id'


class OptionViewSet(CustomViewSet):
    serializer_class = OptionSerializer
    permission_classes = [UserAccessApiBasePermission]
    model = Option
    queryset = Option.objects.all()
    lookup_field = 'hashed_id'


class ExamViewSet(CustomViewSet):
    serializer_class = ExamSerializer
    permission_classes = [UserAccessApiBasePermission]
    model = Exam
    queryset = Exam.objects.all()
    lookup_field = 'hashed_id'


class StudentAnswerSheetViewSet(CustomViewSet):
    serializer_class = StudentAnswerSheetSerializer
    permission_classes = [UserAccessApiBasePermission]
    model = StudentAnswerSheet
    queryset = StudentAnswerSheet.objects.all()
    lookup_field = 'hashed_id'

