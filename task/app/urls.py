from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns=[
    path('<int:pk>',views.StudentView.as_view()),
    path('',views.StudentView.as_view()),
    path('user',views.CreateUser.as_view()),
    path('data/',views.DataView.as_view()),
    path('access/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]