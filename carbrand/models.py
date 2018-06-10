# -*-coding:utf-8-*-
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    creat_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)


class CarBrand(BaseModel):
    name_ch = models.CharField(max_length=64)
    name_en = models.CharField(max_length=128)
    image_url = models.CharField(max_length=1024, blank=True)
    country = models.CharField(max_length=128)
    introduction = models.TextField(blank=False)
    website = models.CharField(max_length=512)

    def __unicode__(self):
        return self.name_ch


class ClassicModel(BaseModel):
    carbrand_ref = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=1024, blank=True)
    guidence_price = models.CharField(max_length=128)

    def __unicode__(self):
        return self.carbrand_ref.name_ch
