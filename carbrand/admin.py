from django.contrib import admin

# Register your models here.

from .models import CarBrand
from .models import Series

admin.site.register(CarBrand)
admin.site.register(Series)
