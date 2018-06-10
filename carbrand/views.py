#from django.core.cache import cache
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import CarBrandSarializers


from models import *
# Create your views here.


# class CarbrandsViewSet(viewsets.ModelViewSet):
#     """
#     query carbrands list
#     """
#     queryset = CarBrand.objects.all()
#     serializer_class = CarBrandSarializers

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

class CarbrandsViewSet(APIView):

    def get(self, format=None):
        carbrand_list = CarBrand.objects.all()
        print carbrand_list
        cs = CarBrandSarializers(carbrand_list, many=True)
        return Response(cs.data)

    def post(self, request, format=None):
        cs = CarBrandSarializers(data=request.data)
        if cs.is_valid():
            cs.save()
            return Response(cs.data, status=status.HTTP_201_CREATED)
        return Response(cs.errors, status=status.HTTP_400_BAD_REQUEST)


class carbrandDetailView(APIView):

    def get_object(self, pk):
        try:
            return CarBrand.object.get(pk=pk)
        except CarBrand.DoesNotExist:
            raise Http404

    def get(self, pk, format=None):
        carbrand = self.get_object(pk)
        cs = CarBrandSarializers(carbrand)
        return Response(cs.data)

    def post(self, request, pk, format=None):
        carbrand = self.get_object(pk)
        cs = CarBrandSarializers(carbrand, data=request.data)
        if cs.is_valid():
            cs.save()
            return Response(cs.data, status=status.HTTP_201_CREATED)
        return Response(cs.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk, format=None):
        carbrand = self.get_object(pk)
        carbrand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
