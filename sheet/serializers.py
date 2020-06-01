from rest_framework import serializers
from .models import Sheet


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