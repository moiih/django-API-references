from django.urls import path
from . import views


urlpatterns = [
    path('basic_response/', views.basic_json_response, name='basic-response'),    
    path('', views.apiOverview, name='api-Overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<int:pk>/', views.taskDetail, name='task-detail'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<int:pk>/', views.taskUpdate, name='task-update'),    
    path('task-delete/<int:pk>/', views.taskDelete, name='task-delete'),
    path('task-patch/<int:pk>/', views.taskPatch, name='task-patch'),
]
