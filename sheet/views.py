from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Sheet
from .forms import SheetForm
from .serializers import SheetListSerializer, SheetDetailSerializer, SheetCreateViewSerializer, \
    SheetUpdateViewSerializer, SheetDeleteViewSerializer, SerchResultsSerializer
from .service import send
from .tasks import send_my_email



class SheetListView(ListView):
    '''Представление списка записей'''
    model = Sheet
    context_object_name = 'sheet_list'
    template_name = 'sheet/sheet_list.html'


class SheetListViewAPI(generics.ListAPIView):
    '''API списка записей'''
    serializer_class = SheetListSerializer
          

class SheetDetailView(DetailView):
    '''Представление отдельной записи'''
    model = Sheet
    context_object_name = 'sheet'
    template_name = 'sheet/sheet_detail.html'


class SheetDetailViewAPI(generics.RetrieveAPIView):
    '''API отдельной записи'''
    serializer_class = SheetListSerializer
    queryset = Sheet.objects.all()


class SheetCreateView(CreateView):
    '''Представление создания записи'''
    model = Sheet
    form_class = SheetForm
    template_name = 'sheet/sheet_add.html'

    def form_valid(self, form):
        form.save()
        # send_my_email.delay(form.instance.title, form.instance.content, form.instance.date_event)
        send_my_email.apply_async((form.instance.title, form.instance.content, form.instance.date_event), eta=(form.instance.date_event - timedelta(hours=1)))
        return super().form_valid(form)


class SheetCreateViewAPI(generics.CreateAPIView):
    '''API создания записи'''
    serializer_class = SheetCreateViewSerializer



class SheetUpdateView(UpdateView):
    '''Представление изменения записи'''
    model = Sheet
    fields = ['title', 'content', 'date_event']
    template_name = 'sheet/sheet_update.html'


class SheetUpdateViewAPI(generics.UpdateAPIView):
    '''API изменения записи'''
    serializer_class = SheetUpdateViewSerializer
    queryset = Sheet.objects.all()


class SheetDeleteViews(DeleteView):
    '''Представление удаления записи'''
    model = Sheet
    template_name = 'sheet/sheet_delete.html'
    success_url = reverse_lazy('list_sheet')


class SheetDeleteViewAPI(generics.DestroyAPIView):
    '''API удаления записи'''
    serializer_class = SheetDeleteViewSerializer
    queryset = Sheet.objects.all()


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


class SerchResultsViewAPI(generics.ListAPIView):
    '''API поиска записей'''
    serializer_class = SerchResultsSerializer
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
