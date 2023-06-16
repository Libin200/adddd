from django.db import models

# Create your models here.
class aaa(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact_no= models.BigIntegerField(max_length=20)
    class Meta:
        db_table="aaa"