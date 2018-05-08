from django.contrib import admin

# Register your models here.

from .models import CarBrand
from .models import CarBrandDetail
from .models import ClassicModel

admin.site.register(CarBrand)
admin.site.register(CarBrandDetail)
admin.site.register(ClassicModel)
