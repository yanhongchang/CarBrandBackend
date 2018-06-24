from rest_framework import serializers
from models import CarBrand, Series


class CarBrandSarializers(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'
        # fields = ('id', 'name')


class SeriesSarializers(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'

