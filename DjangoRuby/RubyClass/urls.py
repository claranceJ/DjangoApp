from django.urls import path
from RubyClass import views


urlpatterns =[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('blogs/', views.blogs, name='blogs'),
    path('services/', views.services, name='services'),
    path('career/', views.career, name='career')
]