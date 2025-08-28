from tkinter import Image
from django.urls import path
from res.views import (HomeView, AboutView, ServiceView, MenuView, TestimonialView, BookingView, TeamView,
                       ContactView, )

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('service/', ServiceView.as_view(), name='service'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('team/', TeamView.as_view(), name='team'),
    path('contact/', ContactView.as_view(), name='contact')
]
