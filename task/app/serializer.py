from rest_framework import serializers
from .models import Subjects, Teacher, Student,User


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for Users """
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.role = validated_data['role']
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username','password','password','role']


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