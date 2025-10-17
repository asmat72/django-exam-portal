from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Exam(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()  # ✅ This must exist
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Option A'),
            ('B', 'Option B'),
            ('C', 'Option C'),
            ('D', 'Option D'),
        ],
        default='A'
    )


from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class StudentExam(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField()
    total = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    time_taken = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(default=timezone.now)


#
class StudentAnswer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='options')
    Selected_option = models.CharField(max_length=1)  # e.g., 'A', 'B', 'C', 'D'

    def __str__(self):
        return f"{self.student.username} - Q{self.question.id}: {self.Selected_option}"

#
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)

