__author__ = "priyanka"

from rest_framework import serializers, status
from django.db import transaction
from datetime import datetime
from artists.models import Artists as ArtistsTbl
from Amazatic.common_functions import CustomAPIException

class ArtistsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtistsTbl
        fields = ('id_string','first_name','last_name','is_active','created_by','created_date')


class ArtistsSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, max_length=200,error_messages={"required": "The field name is required."})
    last_name = serializers.CharField(required=True, max_length=200,error_messages={"required": "The field name is required."})

    class Meta:
        model = ArtistsTbl
        fields = ('id_string','first_name','last_name','is_active','created_by','created_date')

    def create(self, validated_data):
        with transaction.atomic():
            if ArtistsTbl.objects.filter(first_name=validated_data['first_name'], last_name=validated_data['last_name']).exists():
                raise CustomAPIException('ARTISTS_ALREADY_EXIST', status_code=status.HTTP_409_CONFLICT)
            else:
                artist_obj = super(ArtistsSerializer, self).create(validated_data)
                artist_obj.created_by = 1
                artist_obj.created_date = datetime.utcnow()
                artist_obj.save()
                return artist_obj

    def update(self, instance, validated_data):
        if ArtistsTbl.objects.filter(first_name=validated_data['first_name'], last_name=validated_data['last_name']).exists():
            raise CustomAPIException('ARTISTS_ALREADY_EXIST', status_code=status.HTTP_409_CONFLICT)
        else:
            artist_obj = super(ArtistsSerializer, self).update(instance, validated_data)
            artist_obj.updated_by = 1
            artist_obj.updated_date = datetime.utcnow()
            artist_obj.save()
            return artist_obj


