# -*-coding:utf-8-*-
from django.db import models

# Create your models here.


class Country(models.Model):
    country_id = models.CharField(max_length=16)
    country_name_ch = models.CharField(max_length=128, blank=True)
    country_name_en = models.CharField(max_length=128, blank=True)

    def __unicode__(self):
        return self.country_name_ch


class CarBrand(models.Model):
    carbrand_id = models.CharField(max_length=64)
    name_ch = models.CharField(max_length=64)
    name_en = models.CharField(max_length=128, blank=True)
    img = models.CharField(max_length=1024, blank=True)
    introduction = models.TextField(blank=True)
    website = models.CharField(max_length=512, blank=True)
    ranking = models.IntegerField()
    level = models.CharField(max_length=32, default=None)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name_ch


class Series(models.Model):
    carbrand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    image_url = models.CharField(max_length=1024, blank=True)
    guidence_price = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name