from rest_framework import serializers
from models import CarBrand, ClassicModel


class CarBrandSarializers(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'
        # fields = ('id', 'name')


class ClassicModelSarializers(serializers.ModelSerializer):
    class Meta:
        model = ClassicModel
        fields = '__all__'

