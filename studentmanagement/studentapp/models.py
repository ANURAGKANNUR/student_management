from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class State(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name


class District(models.Model):
    name=models.CharField(max_length=250)
    state=models.ForeignKey(State,on_delete=models.CASCADE,related_name='districtview')

    def __str__(self):
        return self.name

class Student(models.Model):
    student_code=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=200)
    email=models.EmailField(max_length=250,unique=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE,related_name='stateview')
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    image=models.FileField(upload_to='studentapp/images/')

    def __str__(self):
        return self.email

