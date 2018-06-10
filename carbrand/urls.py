from django.conf.urls import url
from . import views

# from django.conf.urls import url, include
# from rest_framework import routers
# from . import views


#
# router = routers.DefaultRouter()
# router.register(r'carbrands', views.CarbrandsViewSet)
#
#
# urlpatterns = [
#     url(r'^', include(router.urls)),
# ]

urlpatterns = [
    url(r'^carbrands/', views.CarbrandsViewSet.as_view()),
]
