from django.db import models
from django.utils import timezone

# Create your models here.
class Employee(models.Model):
    E_id=models.IntegerField(blank=True,null=True) 
    E_name=models.CharField(max_length=30)
    E_mail_add=models.EmailField()
    E_sal=models.FloatField()
    E_sal_date=models.DateTimeField(auto_now=True)
    
    
    def sal_date(self):
        self.E_sal_date=timezone.now()
        self.save()
    
    
    def __str__(self):
        return self.E_name



