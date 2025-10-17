from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # or 'home'
    else:
        form = UserCreationForm()
    return render(request, 'exam/register.html', {'form': form})

# 
from django.shortcuts import render

def home_view(request):
    return render(request, 'exam/home.html')

# Dashboard
from django.db.models import Avg, Max
from .models import StudentExam
from django.contrib.auth.decorators import login_required
from .models import Exam, StudentExam

@login_required
def dashboard(request):
    exams = Exam.objects.all()  # ✅ Define exams
    results = StudentExam.objects.filter(student=request.user)
    student_exams = StudentExam.objects.filter(student=request.user)
    all_exams = StudentExam.objects.filter(exam__in=[e.exam for e in student_exams])

    rankings = all_exams.order_by('-score')[:10]  

    return render(request, 'exam/dashboard.html', {
        'student': request.user,
        'exams': exams,
        'results': results,
        'rankings': rankings
    })


# 1 login
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'exam/login.html', {'form': form})

# 2 logout
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')

#
from django.shortcuts import render, get_object_or_404, redirect
from .models import Exam, Question, StudentExam
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam/exam_list.html', {'exams': exams})

# Exam_detail 
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Exam, Question, StudentExam

@login_required
def exam_detail(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    questions = Question.objects.filter(exam=exam)
    student = request.user

    if request.method == 'POST':
        score = 0
        student_answers = {}

        for question in questions:
            selected = request.POST.get(f'question_{question.id}')
            student_answers[question.id] = selected 
            
            if selected == question.correct_answer:
                score += 1
                
        total_questions = questions.count()    
        if total_questions > 0:
            accuracy = round((score / total_questions) * 100, 2)
        else:
            accuracy = 0

        start_time_str = request.session.get('start_time')
        start_time = datetime.fromisoformat(start_time_str)
        time_taken = timezone.now() - start_time

        current_result = StudentExam.objects.create(
            student=request.user,
            exam=exam,
            score=score,
            total=questions.count(),
            time_taken=int(time_taken.total_seconds() // 60),
        )

        if request.headers.get('Accept') == 'application/json':
            exam_data = {
                'title': exam.title,
                'duration': exam.duration,
                'date': exam.date.strftime('%Y-%m-%d') if hasattr(exam, 'date') else None
            } 
            return JsonResponse({'exam': exam_data})
        
        return render(request, 'exam/result.html', {
            'student': student,
            'exam': exam,
            'questions': questions,
            'student_answers': student_answers,
            'score': score,
            'accuracy': accuracy,
            'time_taken': current_result.time_taken,
        })

    # Handle GET: Show the exam page
    request.session['start_time'] = timezone.now().isoformat()

    return render(request, 'exam/exam_detail.html', {'exam': exam, 'questions': questions})


# Result
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Exam, StudentExam  # adjust the import path if models are elsewhere

@login_required
def exam_result(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    student = request.user
    current_result = StudentExam.objects.filter(student=student, exam=exam).last()

    # ✅ Fetch all past results for this student
    results = StudentExam.objects.filter(student=student).select_related('exam')

    return render(request, 'exam/result.html', {
        'exam': exam,
        'student': student,
        'score': current_result.score,
        'accuracy': (current_result.score / exam.questions.count()) * 100,
        'time_taken': current_result.time_taken,
        'results': results  # ✅ pass to template
    })

# 
from django.shortcuts import render
from .models import Exam

def available_exams(request):
    exams = Exam.objects.all()
    return render(request, 'exam/available_exams.html', {'exams': exams})

# 
from .models import Exam, Question

def attempt_exam(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    questions = Question.objects.filter(exam=exam)

    return render(request, 'exam/attempt_exam.html', {
        'exam': exam,
        'questions': questions,
    })

#
from .models import StudentExam

def submit_exam(request, exam_id):
    if request.method == 'POST':
        exam = Exam.objects.get(id=exam_id)
        questions = Question.objects.filter(exam=exam)
        for question in questions:
            Selected = request.POST.get(f'q{question.id}')
            if Selected:
                StudentAnswer.objects.create(
                    question=Question,
                    Selected_option=int(selected),
                    student_id=1  # Replace with actual logged-in student ID
                )
        return render(request, 'exam/thank_you.html')

# 
from .models import Exam, Question, StudentAnswer, StudentExam

def submit_exam(request, exam_id):
    if request.method == 'POST':
        exam = Exam.objects.get(id=exam_id)
        questions = Question.objects.filter(exam=exam)
        correct = 0
        total = questions.count()
        student_id = 1  # Replace with actual logged-in student ID

        for question in questions:
            Selected = request.POST.get(f'question_{question.id}')
            if Selected:
                Selected_option = int(selected)
                StudentAnswer.objects.create(
                    question=Question,
                    Selected_option=selected_option,
                    student_id=student_id
                )
                if selected_option == Question.correct_option_id:
                    correct += 1
      
        score = correct * 1  # 1 mark per question (customize if needed)

        StudentExam.objects.create(
            student_id=student_id,
            exam=exam,
            score=score,
            total_questions=total,
            correct_answers=correct
        )

        return redirect('exam/student_dashboard')

#
from django.db.models import Avg, Max, Count

def student_dashboard(request):
    student_id = 1  # Replace with actual logged-in student ID
    results = StudentExam.objects.filter(student_id=student_id)

    for result in results:
        result.accuracy = round((result.correct_answers / result.total_questions) * 100, 2)

        # Ranking logic
        all_scores = StudentExam.objects.filter(exam=result.exam).order_by('-score')
        rank = list(all_scores.values_list('student_id', flat=True)).index(student_id) + 1
        result.rank = rank
    
    return render(request, 'exam/student_dashboard.html', {'results': results})
   
# Results
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import StudentExam

@login_required
def result(request):
    results = StudentExam.objects.filter(student=request.user)
    return render(request, 'exam/result.html', {'results': results})







