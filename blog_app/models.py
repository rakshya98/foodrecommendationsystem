from django.db import models
from datetime import date
# Create your models here.
class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.CharField(max_length=200)
    title=models.CharField(max_length=50)
    description1=models.CharField(max_length=5000)
    description2=models.TextField()
    description3=models.TextField()
    pub_date=models.DateField(default=date.today)
    thumbnail=models.URLField()
    def __str__(self):
        return self.title
   
   
      