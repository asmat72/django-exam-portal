from django.urls import path
from . import views 
from .admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),    
    path('', views.home_view, name='home'),    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('result/', views.result, name='result'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('exam/', views.exam_list, name='exam_list'),
    path('exam/<int:exam_id>/', views.exam_detail, name='take_exam'),
    path('result/<int:exam_id>/', views.exam_result, name='exam_result'),
    path('exams/', views.available_exams, name='available_exams'),
    path('exam/<int:exam_id>/', views.attempt_exam, name='attempt_exam'),
    path('exam/<int:exam_id>/submit/', views.submit_exam, name='submit_exam'),
    path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
]


