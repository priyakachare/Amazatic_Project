from django.db import models
import uuid  # importing package for guid
from datetime import datetime # importing package for datetime
from django.utils import timezone



class Artists(models.Model):
    id_string = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    created_by = models.BigIntegerField(null=True, blank=True)
    updated_by = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    updated_date = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return str(self.first_name) +" "+ str(self.last_name)

    def __unicode__(self):
        return self.first_name


def get_artist_by_id_string(id_string):
    try:
        return Artists.objects.get(id_string=id_string,is_active=True)
    except Exception as e:
        raise e
    

