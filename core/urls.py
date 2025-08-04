from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('about/', views.about_page, name='about-page'),
]

