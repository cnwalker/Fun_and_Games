import settings
from time import time
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserProfileManager(BaseUserManager):
    def create_user(self, email, phone, password=None):
        """
        Creates and saves a User with the given email, phone,
        and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password):
        """
        Creates and saves a superuser with the given email, phone,
        and password.
        """
        user = self.create_user(email,
            password=password,
            phone=phone
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)

class UserProfile(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        )
    phone = models.CharField(max_length = 25)
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    thumbnail = models.FileField(max_length = 250, blank = True, null=True,
                                 upload_to=get_upload_file_name)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def get_full_name(self):
        # The user is identified by their first and last name
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def email_user(self, subject, message, from_email=None):
        #Sends user an email
        send_mail(subject, message, from_email, [self.email])
    
    # On Python 3: def __str__(self):
    def __unicode__(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.email
        

    def get_topics(self):
        return map(lambda x: x.strip().lower().title(), self.favorite_topics.split(','))

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
##
##    def save(self, *args, **kwargs):
##        if not self.thumbnail:
##            self.thumbnail = "sweg.jpg"
##        super(UserProfile, self).save(*args, **kwargs)

    
