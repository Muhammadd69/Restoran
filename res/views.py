from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import Chefs, Food, Klents


class HomeView(View):
    def get(self, request):
        foods = Food.objects.all()
        chefs = Chefs.objects.all()
        klent = Klents.objects.all()
        context = {
            'foods': foods,
            'chefs': chefs,
            'klent': klent,
        }
        return render(request, 'res/index.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'res/about.html')


class ServiceView(View):
    def get(self, request):
        return render(request, 'res/service.html')


class MenuView(View):
    def get(self, request):
        return render(request, 'res/menu.html')


class TestimonialView(View):
    def get(self, request):
        return render(request, 'res/testimonial.html')


class BookingView(View):
    def get(self, request):
        return render(request, 'res/booking.html')


class TeamView(View):
    def get(self, request):
        return render(request, 'res/team.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'res/contact.html')

    def post(self, request):
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
