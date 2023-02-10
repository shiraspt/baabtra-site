from django.urls import path
from . import views

urlpatterns = [
path ("master",views.master),
path ("aboutus",views.aboutus),
path ("placement",views.placement),
path ("blog",views.blog),
path ("gallery",views.gallery),
path ("home",views.home),
path ("contact",views.contact)



]