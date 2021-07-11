from django.db import models
import uuid  # importing package for guid
from datetime import datetime # importing package for datetime
from django.utils import timezone
from artists.models import Artists
from genres.models import Genres


class Movies(models.Model):
    id_string = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    genre_id = models.ForeignKey(Genres,blank=True, null=True, on_delete=models.SET_NULL)
    artist_id = models.ForeignKey(Artists,blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    created_by = models.BigIntegerField(null=True, blank=True)
    updated_by = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    updated_date = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return str(self.name) +" - "+ str(self.id_string)

    def __unicode__(self):
        return self.name

def get_movie_by_id_string(id_string):
    try:
        return Movies.objects.get(id_string=id_string,is_active=True)
    except Exception as e:
        raise e