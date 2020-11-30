# from django.contrib.auth.models import User
from pydoc import doc

from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Student, Subjects, Teacher
from .serializer import StudentSerializer, SubjectSerializer, UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class CreateUser(APIView):
    def get(self,request):
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True, context={'request': request})
        return Response(serializer.data)

    def patch(self,request,pk=None):
        student = Subjects.objects.get(id=pk)
        serializer = SubjectSerializer(student,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataView(View):
    def get(self,request):
        stu = Student.objects.all()
        template = 'data.html'
        context = {'stu':stu}
        return render(request,template,context)


