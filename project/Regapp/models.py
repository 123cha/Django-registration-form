from django.db import models


class Student(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    usn = models.CharField(max_length=50,default="")
    name = models.CharField(max_length=50,default="")
    sem = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name
