import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):

    # create user
    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()

        return user

    # create super user with admin permissions
    def create_superuser(self, username, email, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300, null=True)
    username = models.CharField(max_length=300, null=True, unique=True, db_index=True)
    email = models.EmailField(max_length=300, unique=True, null=True, db_index=True)
    password = models.CharField(max_length=1000, default='password')
    last_login = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=False)
    login_count = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=15, null=True)
    last_login_ip = models.CharField(max_length=300, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return str(self.email)

    @property
    def token(self):
        return str(self._generate_jwt_token())

    def get_full_name(self):
        return str(self.username)

    def get_short_name(self):
        return str(self.username)

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return str(token.decode('utf-8'))

    class Meta:
        db_table = 'farm_user_user'


class BlackListedToken(models.Model):
    token = models.CharField(max_length=600)
    user = models.ForeignKey(User, related_name="token_user", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("token", "user")