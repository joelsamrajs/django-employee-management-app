from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Leave, Profile, FamilyMember

# Unregister models here.
admin.site.unregister(Group)
admin.site.register(Leave)

admin.site.register(Profile)
admin.site.register(FamilyMember)