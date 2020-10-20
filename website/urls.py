from django.urls import path
from .import views

urlpatterns = [
  path('',views.home,name='home'),
  path('services/',views.services,name='services'),
  path('portfolio/',views.portfolio,name='portfolio'),
  path('blog/',views.blog,name='blog'),
  path('contacts/',views.contact,name='contacts'),
  path('aboutus/',views.about,name='aboutus'),
]
