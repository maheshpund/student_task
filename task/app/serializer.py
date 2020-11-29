from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Subjects, Teacher, Student
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        print(validated_data)
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','password','password']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['id','subject_name']


class TeacherSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = Teacher
        fields = ['id','teacher_name','subjects']


class StudentSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    class Meta:
        model = Student
        fields = ['id','student_name','teachers']