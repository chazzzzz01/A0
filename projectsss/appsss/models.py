# appsss/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('employee', 'Employee'),
        ('staff', 'Staff'),
    ]

    DEPARTMENT_CHOICES = [
        ('STCS', 'School of Technology and Computer Science'),
        ('SCJE', 'School of Criminal Justice and Education'),
        ('SAS', 'School of Arts and Sciences'),
        ('SME', 'School of Management and Entrepreneurship'),
        ('SOE', 'School of Engineering'),
        ('SNHS', 'School of Nursing and Health Sciences'),
        ('LHS', 'Liberal Arts and Humanities'),
        ('STED', 'School of Teacher Education'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    department = models.CharField(max_length=5, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    student_id_image = models.ImageField(upload_to='student_ids/', blank=True, null=True)
    study_load_image = models.ImageField(upload_to='study_loads/', blank=True, null=True)
    employee_id_image = models.ImageField(upload_to='employee_ids/', blank=True, null=True)
    document_image = models.ImageField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.user.username
