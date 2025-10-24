# Online Examination Portal (Django + SQLite)

- 📌 Project Description:
  - This project is a web-based Online Examination Portal built using Django and SQLite. It enables:
    - Administrators to create, manage, and monitor exams.
    - Students to register, log in, and attempt multiple-choice exams within a defined time limit.
    - The system automatically calculates scores and generates performance reports.

- ✨ Features:
    - 🔐 Secure login and registration for students and administrators using Django’s authentication system.
    -  Admin dashboard to:
       - Create, update, and delete exams.
       - Add multiple-choice questions and mark correct answers.
    -  Student dashboard to:
       - Register and log in.
       - Attempt exams within a time limit.
    - 📊 Automatic score calculation for objective-type questions.
    - 📈 Performance reports showing:
       - Total marks
       - Accuracy
       - Ranking

- 🛠️ Tech Stack:
       Layer:     	    Technology:
    - Backend         	Django (Python)
    - Database	        SQLite
    - Frontend	        HTML, CSS, Bootstrap.

- 📁 Project Structure:
    
      - ├── exam_portal/              # Main Django app
      -      ├── exam/
      -      │    ├── migrations/           # Database migrations
      -      │    ├── templates/            # HTML templates
      -      │    │   ├── base.html
      -      │    │   ├── login.html
      -      │    │   ├── register.html
      -      │    │   ├── dashboard.html
      -      │    │   └── exam.html
      -      │    ├── static/               # CSS, JS, Bootstrap assets
      -      │    ├── admin.py              # Admin interface setup
      -      │    ├── models.py             # Database models
      -      │    ├── views.py              # View logic
      -      │    ├── urls.py               # URL routing
      -      │    └── forms.py              # Django forms
      -      ├── db.sqlite3                # SQLite database
      -      ├── manage.py                 # Django management script
      -      └── README.md                 # Project documentation

- 🧩 Custom Dataset Explanation:
     - To support exams, questions, answers, and student results, define these models in models.py:
        1. Exam:
           - Stores exam metadata.
           -   class Exam(models.Model):
           -   title = models.CharField(max_length=100)
           -   duration = models.IntegerField(help_text="Duration in minutes")
              
        2. Question:
           - Stores multiple-choice questions linked to an exam.
             - class Question(models.Model):
             -     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
             -     text = models.TextField()
             -     option1 = models.CharField(max_length=200)
             -     option2 = models.CharField(max_length=200)
             -     option3 = models.CharField(max_length=200)
             -     option4 = models.CharField(max_length=200)
             -     correct_option = models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')])

        3. Student:
           - Extends Django’s user model with student-specific fields.
             - class Student(models.Model):
             -     user = models.OneToOneField(User, on_delete=models.CASCADE)
             -     roll_number = models.CharField(max_length=20)

        4. Result:
           - Stores student performance data.
             - class Result(models.Model):
             -     student = models.ForeignKey(Student, on_delete=models.CASCADE)
             -     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
             -     score = models.IntegerField()
             -     accuracy = models.FloatField()
             -     rank = models.IntegerField()

- 🔗 Dataset Link:
     - If you have a dataset file (CSV, JSON, etc.) containing questions, answers, and student records, you can import it using Django’s manage.py shell or a custom script. Let me know if you'd like help writing that script!

- 🎯 Learning Outcomes
     - By completing this project, you will:
       - ✅ Learn to build dynamic web interfaces using Django.
       - ✅ Understand how to integrate backend logic with frontend design.
       - ✅ Gain hands-on experience with secure authentication and user management.
       - ✅ Master the full development lifecycle: building, testing, and deploying a real-world web application.
       - ✅ Learn to model and manage relational data using Django ORM and SQLite.
        
