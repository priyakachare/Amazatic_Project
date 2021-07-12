import uuid
from datetime import datetime
from django.utils import timezone  # importing package for datetime
from django.db import models
from rest_framework import serializers, status
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# Create USER Master table start.
class User(AbstractBaseUser, PermissionsMixin):
    username = None
    id_string = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.CharField(max_length=200, unique=True)
    USERNAME_FIELD = ('email')
    password = models.CharField(max_length=200, verbose_name='password')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_by = models.BigIntegerField(null=True, blank=True)
    updated_by = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    updated_date = models.DateTimeField(null=True, blank=True)

    objects = MyUserManager()
    REQUIRED_FIELDS = []

