from django.db import models

# Create your models here.

# class Company(models.Model):
#     company=models.ForeignKey(User,on_delete=models.CASCADE)
#     Agent=models.CharField(max_length=50,null=True)
    
class Company_name(models.Model):
    com_name=models.CharField(max_length=50,null=True)
    com_location=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.com_name

class Agent_name(models.Model):
    company=models.ForeignKey(Company_name,on_delete=models.CASCADE)
    emp_name=models.CharField(max_length=50,null=True) 
    call_atd=models.IntegerField()
    time_dur=models.TimeField()       

    def __str__(self):
        return self.emp_name