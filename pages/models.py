from operator import mod
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.utils import timezone
# Create your models here.

LEAVE_TYPES = (
    ("CASUAL", "CASUAL"),
    ("SICK", "SICK"),
    ("PRIVILEGE", "PRIVILEGE"),
)

FAMILY_RELATIONSHIPS = (
    ("FATHER", "FATHER"),
    ("MOTHER", "MOTHER"),
    ("SIBLING", "SIBLING"),
    ("SON", "SON"),
)


def employee_photo_upload(instance, filename):
        return 'employee_photo/{0}_{1}'.format(instance.name, filename)


class Profile(models.Model):
    name = models.CharField(max_length=200, unique=True,)
    date_of_birth = models.DateField(blank=False)
    address = models.TextField(blank=True)
    email_id = models.EmailField(max_length=256, unique=True,)
    photo = models.ImageField(upload_to=employee_photo_upload, null=True, blank=True,)
    salary = models.IntegerField(blank=False)
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)

    def get_absolute_url(self):
        return reverse('profile-update', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s" % (self.name) 


class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50, choices=FAMILY_RELATIONSHIPS)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    email_id = models.EmailField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

class Leave(models.Model):
    #employee_name = models.CharField(max_length=200, )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    leave_date = models.DateField(max_length=200, blank=False)   
    leave_type = models.CharField(max_length=50, choices=LEAVE_TYPES, blank=False)

    class Meta:
        unique_together = ('profile', 'leave_date',)

    def __str__(self):
        return '%s: %a' % (self.leave_date, self.leave_type)
