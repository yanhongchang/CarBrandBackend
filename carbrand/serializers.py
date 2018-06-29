from rest_framework import serializers
from models import CarBrand, Series,Country


class CarBrandSarializers(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.country_name_cn')

    class Meta:
        model = CarBrand
        fields = ('carbrand_id', 'name_cn', 'img', 'ranking', 'level', 'country', 'country_name')


class SeriesSarializers(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'


class CountrySarializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
