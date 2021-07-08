__author__ = "priyanka"

from rest_framework import serializers, status
from django.db import transaction
from datetime import datetime
from genres.models import Genres as GenresTbl
from Amazatic.common_functions import CustomAPIException

class GenresListSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenresTbl
        fields = ('id_string','name','is_active','created_by','created_date')


class GenresSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=200,error_messages={"required": "The field name is required."})

    class Meta:
        model = GenresTbl
        fields = ('id_string','name','is_active','created_by','created_date')

    def create(self, validated_data):
        with transaction.atomic():
            if GenresTbl.objects.filter(name=validated_data['name']).exists():
                raise CustomAPIException('GENRES_ALREADY_EXIST', status_code=status.HTTP_409_CONFLICT)
            else:
                genre_obj = super(GenresSerializer, self).create(validated_data)
                genre_obj.created_by = 1
                genre_obj.created_date = datetime.utcnow()
                genre_obj.save()
                return genre_obj

    def update(self, instance, validated_data):
        if GenresTbl.objects.filter(name=validated_data['name']).exists():
            raise CustomAPIException('GENRES_ALREADY_EXIST', status_code=status.HTTP_409_CONFLICT)
        else:
            genre_obj = super(GenresSerializer, self).update(instance, validated_data)
            genre_obj.updated_by = 1
            genre_obj.updated_date = datetime.utcnow()
            genre_obj.save()
            return genre_obj


