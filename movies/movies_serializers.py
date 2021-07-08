__author__ = "priyanka"

from rest_framework import serializers, status
from django.db import transaction
from datetime import datetime
from movies.models import Movies as MoviesTbl
from Amazatic.common_functions import CustomAPIException, get_validate_data

class MoviesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoviesTbl
        fields = ('id_string','name','genre_id','artist_id','is_active','created_by','created_date')


class MoviesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=200,error_messages={"required": "The field name is required."})
    artist_id = serializers.CharField(required=True, max_length=200,error_messages={"required": "The field name is required."})
    genre_id = serializers.CharField(required=True, max_length=200,error_messages={"required": "The field name is required."})


    class Meta:
        model = MoviesTbl
        fields = ('id_string','name','artist_id','genre_id','is_active','created_by','created_date')

    def create(self, validated_data):
        with transaction.atomic():
            validated_data = get_validate_data(validated_data)
            if MoviesTbl.objects.filter(name=validated_data['name']).exists():
                raise CustomAPIException('MOVIES_ALREADY_EXIST', status_code=status.HTTP_409_CONFLICT)
            else:
                movie_obj = super(MoviesSerializer, self).create(validated_data)
                movie_obj.created_by = 1
                movie_obj.created_date = datetime.utcnow()
                movie_obj.save()
                return movie_obj

    def update(self, instance, validated_data):
        if MoviesTbl.objects.filter(name=validated_data['name']).exists():
            raise CustomAPIException('MOVIES_ALREADY_EXIST', status_code=status.HTTP_409_CONFLICT)
        else:
            movie_obj = super(MoviesSerializer, self).update(instance, validated_data)
            movie_obj.updated_by = 1
            movie_obj.updated_date = datetime.utcnow()
            movie_obj.save()
            return movie_obj


