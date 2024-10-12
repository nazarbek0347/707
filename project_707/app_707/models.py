from django.db import models

# Create your models here.

class Taomlar(models.Model):
    taom_nomi=models.CharField(max_length=200,blank=False)
    taom_narxi=models.IntegerField(blank=False)
    taom_rasmi=models.ImageField(upload_to='media')
    taom_malumoti=models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.taom_nomi

class Ichimliklar(models.Model):
    ichimlik_nomi=models.CharField(max_length=200,blank=False)
    ichimlik_narxi=models.IntegerField(blank=False)
    ichimlik_rasmi=models.ImageField(upload_to='media')

    def __str__(self):
        return self.ichimlik_nomi