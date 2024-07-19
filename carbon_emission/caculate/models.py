from django.db import models

# Create your models here.
class TestDB(models.Model):
    name = models.CharField(max_length=100, null=False)
    distance = models.CharField(max_length=1000000,null=False)
    teu = models.CharField(max_length=1000000,default='1', null=False)
    carbon = models.CharField(max_length=1000000,default='1',null=False)
 
    def __str__(self):
        return self.name