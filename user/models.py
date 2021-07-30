from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser , PermissionsMixin, BaseUserManager
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save()

        return user

    def create_staffuser(self, username, password=None):
        if username is None:
            raise TypeError('Users must have a username.')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username            = models.CharField(max_length=255, blank=False, null=False, unique=True)

    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    last_login          = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.username)
