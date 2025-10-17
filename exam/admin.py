from django.contrib.admin import AdminSite
from django.contrib import admin

class MyAdminSite(AdminSite):
    site_header = "Welcome, Admin"
    site_title = "Exam Portal Admin"
    index_title = "Manage Exams and Users"

admin_site = MyAdminSite(name='myadmin')

# 
from .models import Exam, Question, StudentExam
from .models import Post, Comment

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class ExamAdmin(admin.ModelAdmin):
     list_display = ['title', 'duration']

class StudentExamAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'score', 'time_taken')


admin.site.register(Exam, ExamAdmin)
admin.site.register(Question)
admin.site.register(StudentExam, StudentExamAdmin)
admin.site.register(Post)
admin.site.register(Comment)
