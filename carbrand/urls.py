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
    url(r'^carbrands/$', views.CarbrandListView.as_view()),
    url(r'carbrands/(?P<name>.+)/$', views.CarbrandListView.as_view()),
    url(r'^carbrand/(?P<pk>[0-9]+)/$', views.CarbrandDetailView.as_view()),
]
