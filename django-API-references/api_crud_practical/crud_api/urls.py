from django.urls import path
from . import views


urlpatterns = [
    path('student-api/', views.student_api, name='student-api'),
    # path('student-api/', views.StudentAPI.as_view(), name='student-api'),
]
