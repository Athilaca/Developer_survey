from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

class Answer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='answers')
    question_text = models.CharField(max_length=255)
    answer_text = models.TextField(max_length=512)

    def __str__(self):
        return f"{self.question_text}: {self.answer_text}"