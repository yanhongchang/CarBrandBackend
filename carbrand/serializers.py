from rest_framework import serializers
from models import CarBrand,ClassicModel,CarBrandDetail


class CarBrandSarializers(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'
        # fields = ('id', 'name')

