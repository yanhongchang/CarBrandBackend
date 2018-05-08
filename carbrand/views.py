#from django.core.cache import cache
from rest_framework import viewsets
from serializers import CarBrandSarializers


from models import *
# Create your views here.


class CarbrandsViewSet(viewsets.ModelViewSet):
    """
    query carbrands list
    """
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSarializers

#
# class CarbrandListView(StatusWrapMixin, MultipleJsonResponseMixin, ListView):
#     model = CarBrand
#
#
# class CarbrandDetailView(DetailView):
#
#     pk_url_kwarg = 'id'
#
#     def get_object(self, queryset=None):
#         obj = super(CarbrandDetailView, self).get_object(queryset)
#         #cache.set(obj.id, ob)
#         return obj


