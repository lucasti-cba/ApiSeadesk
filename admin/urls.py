from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',
         views.index,
         name ='admin-index'),
    path('landing/',
         views.landing,
         name ='admin-landing'),
    path('addLanding/',
         views.addLanding,
         name ='admin-addLanding'),
    path('addCarrocel/',
         views.addCarrocel,
         name ='admin-addCarrocel'),
    path('delCarrocel/<int:id>',
         views.delCarrocel,
         name ='admin-delCarrocel'),
    path('service/',
         views.service,
         name ='admin-service'),
     path('addService/',
         views.addService,
         name ='admin-addService'),
    path('delService/<int:id>',
         views.delService,
         name ='admin-delService'),
     path('addTag/',
         views.addTag,
         name ='admin-addTag'),
]

