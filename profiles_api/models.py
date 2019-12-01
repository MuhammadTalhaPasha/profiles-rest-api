from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email ,firstname ,lastname ,password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('User must have a Email Address')

        email = self.normalize_email(email)
        user = self.model(email=email, firstname=firstname, lastname=lastname,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email ,firstname ,lastname ,password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email ,firstname ,lastname ,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname']

    def get_full_name(self):
        """Retrieve full name for user"""
        full_name = firstname +' '+ lastname
        return self.full_name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.firstname

    def __str__(self):
        """Return string representation of user"""
        return self.email

class ProfileFeedItem(models.Model):
    """profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
