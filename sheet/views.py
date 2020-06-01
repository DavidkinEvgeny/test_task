from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.mail import send_mail
from .models import Sheet
from .forms import SheetForm


class SheetListView(ListView):
    '''Представление списка записей'''
    model = Sheet
    context_object_name = 'sheet_list'
    template_name = 'sheet/sheet_list.html'


class SheetDetailView(DetailView):
    '''Представление отдельной записи'''
    model = Sheet
    context_object_name = 'sheet'
    template_name = 'sheet/sheet_detail.html'


class SheetCreateView(CreateView):
    '''Представление создания записи'''
    model = Sheet
    form_class = SheetForm
    template_name = 'sheet/sheet_add.html'

    def form_valid(self, form):
        form.save()
        send_mail(
        form.instance.title,
        f'Текст сообщения: {form.instance.content}, Дата:{form.instance.date_event}',
        'davidkinevgeny@gmail.com',
        ['realtordavidkin@gmail.com'],
        fail_silently=False,
    )
        return super().form_valid(form)


class SheetUpdateView(UpdateView):
    '''Представление изменения записи'''
    model = Sheet
    fields = ['title', 'content', 'date_event']
    template_name = 'sheet/sheet_update.html'


class SheetDeleteViews(DeleteView):
    '''Представление удаления записи'''
    model = Sheet
    template_name = 'sheet/sheet_delete.html'
    success_url = reverse_lazy('list_sheet')


class SerchResultsView(ListView):
    '''Представление поиска'''
    model = Sheet
    context_object_name = 'sheet_list'
    template_name = 'sheet/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('title')
        guery_date = self.request.GET.get('date')
        delta_month = timezone.now() - timedelta(days=30)
        delta_week = timezone.now() - timedelta(days=7)
        delta_day = timezone.now() - timedelta(days=1)
        if guery_date == 'day':
            return Sheet.objects.filter(title__icontains=query, date_event__gte=delta_day)
        elif guery_date == 'week':
            return Sheet.objects.filter(title__icontains=query, date_event__gte=delta_week)
        elif guery_date == 'month':
            return Sheet.objects.filter(title__icontains=query, date_event__gte=delta_month)
        elif guery_date == 'all':
            return Sheet.objects.filter(title__icontains=query)

