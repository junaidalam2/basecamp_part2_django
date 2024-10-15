from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

class CustomUserManager(BaseUserManager):
    """Custom user manager where email is the unique identifier instead of username."""
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular user with the given email and password."""
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a superuser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Custom user model where email is the unique identifier instead of username."""
    
    username = None  # Disable username
    email = models.EmailField(_("email address"), max_length=100, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)

    USERNAME_FIELD = "email"  # Set email as the username field
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Fields required on superuser creation

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'