from django.db import models

# Create your models here.

class Student(models.Model):
    Ano=models.CharField(max_length=100)
    Sname = models.CharField(max_length=250)
    Sphoto=models.FileField()
    Fname = models.CharField(max_length = 250)
    Fphoto=models.FileField()
    Mname = models.CharField(max_length = 250)
    Mphoto=models.FileField()
    School = models.CharField(max_length = 500)
    Grade = models.CharField(max_length=100)
    PYmarks=models.FileField()
    PPYmarks=models.FileField()
    Marks=models.CharField(max_length=100)
    Incomecert=models.FileField()
    Foccup=models.CharField(max_length=100)
    Moccup=models.CharField(max_length=100)
    Sfee=models.CharField(max_length=100)
    Scholar=models.CharField(max_length=100)

    def __str__(self):
        return self.Sname