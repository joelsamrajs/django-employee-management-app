from dataclasses import fields
import imp
import django_filters
from django.db.models import Q
from pages.models import *

class ProfileFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filterSearch',label="Search Name/Email/Id")
    date_of_birth = django_filters.DateFilter(method='filterDateOfBirth',label="Date Of Birth")
    salary = django_filters.CharFilter(method='filterSalary',label="Salary")
    order = django_filters.OrderingFilter(
        fields=(
            ('id', 'id'),
            ('name', 'name'),
            ('salary', 'salary'),
            # and any model field you want to sort based on
        ),
        field_labels={
            'id': 'id',
            'name': 'name',
            'salary': 'salary',
        }
    )
    class Meta:
        model = Profile
        fields = ['search', 'date_of_birth', 'salary']

    def filterSearch(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(id__icontains=value) | Q(email_id__icontains=value)
        )  
    def filterDateOfBirth(self, queryset, name, value):
        return queryset.filter(
            Q(date_of_birth=value)
        )
    def filterSalary(self, queryset, name, value):
        return queryset.filter(
            Q(salary=value)
        )
  

class LeaveFilter(django_filters.FilterSet):
    order = django_filters.OrderingFilter(
        fields=(
            ('profile', 'profile'),
            ('leave_date', 'leave_date'),
            ('leave_type', 'leave_type'),
            # and any model field you want to sort based on
        ),
        field_labels={
            'id': 'id',
            'name': 'name',
        }
    )
    class Meta:
        model = Leave
        fields = ['profile', 'leave_date', 'leave_type']
