from django.urls import path, include
from rest_framework import routers
from apps.exam.api.v1.viewsets import (CourseViewSet,
                                       QuestionViewSet,
                                       OptionViewSet,
                                       ExamViewSet,
                                       StudentAnswerSheetViewSet)


router = routers.DefaultRouter()
router.register('course', CourseViewSet)
router.register('question', QuestionViewSet)
router.register('option', OptionViewSet)
router.register('exam', ExamViewSet)
router.register('student-answer-sheet', StudentAnswerSheetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
