from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    readers = models.CharField(max_length = 20, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Students(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=20)
    student_DOB = models.DateTimeField(blank =True, null=True, default=timezone.now)
    student_subjects = models.CharField(max_length = 20, blank =True, null=True)

    def __str__(self):
        return self.student_name

class Teachers(models.Model):
    teacher_name = models.CharField(max_length=20)
    teacher_subject = models.CharField(max_length=20)
    
    def __str__(self):
        return self.teacher_name





