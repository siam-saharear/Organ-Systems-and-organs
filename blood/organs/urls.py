from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.organ_home, name = "organ_home"),
    path("add_organ/", views.add_organ, name = "add_organ"),
    path("search_organ/", views.search_organ, name = "search_organ"),
    # path("<str>:organ", views.individual_organ, name = "individual_organ")
    re_path(r'^(?P<organ_system>skeletal|respiratory|circulatory|muscular|digestive|nervous)$', views.individual_organ_system, name='individual_organ'),
    re_path(r'^(?P<organ_system>skeletal|respiratory|circulatory|muscular|digestive|nervous)/(?P<organ>[^/]+)$', views.individual_organ, name='individual_organ')
    # re_path(r'^(?P<organ_name>skeletal|respiratory|circulatory|muscular|digestive|nervous)$', views.individual_organ, name='individual_organ'),

]
