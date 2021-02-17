from rest_framework import serializers

from apps.exam.models import Course, Question, Option, Exam, StudentAnswerSheet, StudentExamResult


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class StudentAnswerSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswerSheet
        fields = '__all__'


class StudentExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExamResult
        fields = '__all__'
