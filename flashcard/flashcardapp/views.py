from django.conf import settings
from django.contrib import messages
from django.template.loader import get_template
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic
from .models import *
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'login.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'toppage.html'


class DemoTopPage(generic.ListView):
    model = Category
    template_name = 'demotoppage.html'
    def get_queryset(self):
        q = Category.objects.all()
        return q

class DemoMainPage(generic.ListView):
    model = Card
    template_name = 'demomainpage.html'
    
    def get_queryset(self):
        mode = self.request.GET.get('mode')
        category_id = self.request.GET.get('category')
        category = get_object_or_404(Category, id=category_id)
        all_cards = Card.objects.filter(category = category)
        return all_cards

    def get_context_data(self, **kwargs):
        ctx = super(DemoMainPage, self).get_context_data(**kwargs)
        category_id = self.request.GET.get('category')
        category = get_object_or_404(Category, id=category_id)
        ctx['category'] = category
  
        return ctx

class TopPage(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = 'toppage.html'
    def get_queryset(self):
        q = Category.objects.all()
        return q

class MainPage(LoginRequiredMixin, generic.ListView):
    model = Card
    template_name = 'mainpage.html'
    
    def get_queryset(self):
        mode = self.request.GET.get('mode')
        category_id = self.request.GET.get('category')
        category = get_object_or_404(Category, id=category_id)
        all_cards = Card.objects.filter(category = category)
        if mode == 'mistaken-only':
            only_mistaken = set()
            for mistaken in CardMistaken.objects.filter(user = self.request.user).select_related('card'):
                only_mistaken.add(mistaken.card)
            return only_mistaken
        return all_cards

    def get_context_data(self, **kwargs):
        ctx = super(MainPage, self).get_context_data(**kwargs)
        category_id = self.request.GET.get('category')
        category = get_object_or_404(Category, id=category_id)
        ctx['category'] = category
        ctx['mistakenonly'] = self.request.GET.get('mode') == 'mistaken-only'
        return ctx

def AddMistaken(request):
    card_id = request.POST.get('card_id')
    card = get_object_or_404(Card, id=card_id)
    new_mistaken = CardMistaken()
    new_mistaken.user = request.user
    new_mistaken.card = card
    new_mistaken.save()

    return JsonResponse({'success': True })

def RemoveMistaken(request):
    card_id = request.POST.get('card_id')
    card = get_object_or_404(Card, id=card_id)
    mistaken = CardMistaken.objects.filter(user = request.user, card = card)
    mistaken.delete()

    return JsonResponse({'success': True })
