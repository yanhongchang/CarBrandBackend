#from django.core.cache import cache
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from rest_framework.pagination import PageNumberPagination
#from rest_framework import mixins
#from rest_framework import generics
from serializers import CarBrandSarializers
from rest_framework.renderers import JSONRenderer


from forms import CarbrandResource
from models import *


class MyPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "pagesize"
    max_page_size = 1000
    page_query_param = "page"

# ---- APIView version (new) -----
class CarbrandListView(APIView):

    renderer_classes = (JSONRenderer,)

    @staticmethod
    def get_objects(name):
        try:
            return CarBrand.objects.filter(name_cn__contains=name)
        except CarBrand.DoesNotExist:
            raise Http404

    def get(self, request, name=None):
        if name is None:
            carbrands = CarBrand.objects.all()
        else:
            carbrands = self.get_objects(name)

        if carbrands:
            code = 0
        else:
            code = 1
        resp_data = {'code': code}
        resp_data['msg'] = ''
        resp_data['data'] = {}
        resp_data['data']['carList'] = []

        pg = MyPageNumberPagination()
        carbrands = pg.paginate_queryset(queryset=carbrands, request=request, view=self)

        for carbrand in carbrands:
            carbrand_dict = CarbrandResource(carbrand).to_list_dict()
            resp_data['data']['carList'].append(carbrand_dict)
        print resp_data
        return Response(resp_data)


class CarbrandDetailView(APIView):
    """ carbrand detail function """

    renderer_classes = (JSONRenderer,)

    def get_object(self, pk):
        try:
            if pk in cache:
                return cache.get(pk)
            else:
                carbrand_detail = CarBrand.objects.get(pk=pk)
                cache.set(pk, carbrand_detail, 15 * 60)
                return carbrand_detail
        except CarBrand.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        carbrand_detail = self.get_object(pk)
        if carbrand_detail:
            code = 0
        else:
            code = 1
        carbrand_detail_dict = CarbrandResource(carbrand_detail)\
            .to_detail_dict()
        resp_data = {'code': code}
        resp_data['msg'] = ''
        resp_data['data'] = {}
        resp_data['data']['carDetail'] = carbrand_detail_dict

        return Response(resp_data)

    def put(self, request, pk):
        carbrand = self.get_object(pk)
        print carbrand
        cs = CarBrandSarializers(carbrand, data=request.data)
        if cs.is_valid():
            cs.save()
            return Response(cs.data, status=status.HTTP_201_CREATED)
        return Response(cs.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     print pk
    #     carbrand = self.get_object(pk)
    #     carbrand.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



# ---- model view set  ----

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
#
#


# ---- APIView old -----

# class CarbrandsViewSet(APIView):
#
#     def get(self, format=None):
#         carbrand_list = CarBrand.objects.all()
#         cs = CarBrandSarializers(carbrand_list, many=True)
#         return Response(cs.data)
#
#     def post(self, request, format=None):
#         cs = CarBrandSarializers(data=request.data)
#         if cs.is_valid():
#             cs.save()
#             return Response(cs.data, status=status.HTTP_201_CREATED)
#         return Response(cs.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CarbrandDetailView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return CarBrand.objects.get(pk=pk)
#         except CarBrand.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format= None ):
#         print pk
#         carbrand = self.get_object(pk)
#         cs = CarBrandSarializers(carbrand)
#         return Response(cs.data)
#
#     def put(self, request, pk, format=None):
#         carbrand = self.get_object(pk)
#         print carbrand
#         cs = CarBrandSarializers(carbrand, data=request.data)
#         if cs.is_valid():
#             cs.save()
#             return Response(cs.data, status=status.HTTP_201_CREATED)
#         return Response(cs.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         print pk
#         carbrand = self.get_object(pk)
#         carbrand.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class CarbrandsViewSet(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#
#     queryset = CarBrand.objects.all()
#     serializer_class = CarBrandSarializers
#
#     def get(self, request, *args, **kwargs):
#         #return self.list(request, *args, **kwargs)
#         carbrands = CarBrand.objects.all()
#         print carbrands
#
#     def post(self, request, *args, **kwargs):
#         return self.creat(request, *args, **kwargs)
#
#
# class CarbrandDetailView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return CarBrand.objects.get(pk=pk)
#         except CarBrand.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format= None ):
#         print pk
#         carbrand = self.get_object(pk)
#         cs = CarBrandSarializers(carbrand)
#         return Response(cs.data)
#
#     def put(self, request, pk, format=None):
#         carbrand = self.get_object(pk)
#         print carbrand
#         cs = CarBrandSarializers(carbrand, data=request.data)
#         if cs.is_valid():
#             cs.save()
#             return Response(cs.data, status=status.HTTP_201_CREATED)
#         return Response(cs.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         print pk
#         carbrand = self.get_object(pk)
#         carbrand.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
