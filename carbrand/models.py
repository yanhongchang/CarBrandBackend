# -*-coding:utf-8-*-
from django.db import models

# Create your models here.


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_name_cn = models.CharField(max_length=128, blank=True, null=True)
    country_name_en = models.CharField(max_length=128, blank=True, null=True)

    def __unicode__(self):
        return self.country_name_cn


class CarBrand(models.Model):
    carbrand_id = models.IntegerField(primary_key=True)
    name_cn = models.CharField(max_length=64)
    name_en = models.CharField(max_length=128, blank=True, null=True)
    img = models.CharField(max_length=1024, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=512, blank=True, null=True)
    ranking = models.IntegerField()
    level = models.CharField(max_length=32, blank=True, null=True)
    country = models.ForeignKey(Country, related_name='country', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name_cn


class Series(models.Model):
    carbrand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    image_url = models.CharField(max_length=1024, blank=True, null=True)
    guidence_price = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
