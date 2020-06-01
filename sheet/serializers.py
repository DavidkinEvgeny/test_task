from rest_framework import serializers
from .models import Sheet
from .tasks import send_my_email
from datetime import datetime, timedelta


class SheetListSerializer(serializers.ModelSerializer):
    '''Список записей'''
    class Meta:
        model = Sheet
        fields = ('id', 'title', 'content', 'date_crate', 'date_event')


class SheetDetailSerializer(serializers.ModelSerializer):
    '''Отдельная запись'''
    class Meta:
        model = Sheet
        fields = ['id', 'title', 'content', 'date_crate', 'date_event']


class SheetCreateViewSerializer(serializers.ModelSerializer):
    '''Создание записи'''
    class Meta:
        model = Sheet
        fields = ['title', 'content', 'date_event']
    
    def validate(self, data):
        # send_my_email.delay(data['title'], data['content'], data['date_event'])
        send_my_email.apply_async((data['title'], data['content'], data['date_event']), eta=(data['date_event'] - timedelta(hours=1)))
        return super().validate(data)

class SheetUpdateViewSerializer(serializers.ModelSerializer):
    '''Обновление записи'''
    class Meta:
        model = Sheet
        fields = ['title', 'content', 'date_event']

class SheetDeleteViewSerializer(serializers.ModelSerializer):
    '''Удаление записи'''
    class Meta:
        model = Sheet
        fields = '__all__'


class SerchResultsSerializer(serializers.ModelSerializer):
    '''Список поиска'''
    class Meta:
        model = Sheet
        fields = ('id', 'title', 'content', 'date_crate', 'date_event')