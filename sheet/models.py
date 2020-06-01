from django.db import models
from django.urls import reverse


class Sheet(models.Model):
    '''Модель листка записей'''
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    date_crate = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    date_event = models.DateTimeField(verbose_name='Дата мероприятия')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail_sheet', kwargs={'pk': self.pk})
