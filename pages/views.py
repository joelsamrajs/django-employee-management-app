from msilib.schema import File
from django.shortcuts import redirect, render
from .models import FamilyMember, Leave, Profile
import requests
from .forms import LeaveForm, ProfileForm
from django.contrib import messages
from rest_framework.response import Response
from .forms import FamilyMemberFormSet
from api.filters import ProfileFilter, LeaveFilter


def home(request):
    if request.user.is_authenticated:
        return render(request, 'pages/home.html')
    else:
        return redirect('/login/')


############## 1. PROFILE 👥 ###################
# 1. Profile List 
# 2. Profile Detail 
# 3. Profile Add  
# 4. Profile Edit 
# 5. Profile Delete



# _________ 👥 1.1 Profile List 📃 _________________
def profileList(request):
    if request.user.is_authenticated:
        api_profile_list = requests.get('http://127.0.0.1:8000/api/profile/')
        profile_list = api_profile_list.json()
        profile_filter = ProfileFilter()
        
        if request.method == 'GET':
            query_string = request.META['QUERY_STRING']
            api_profile_list = requests.get('http://127.0.0.1:8000/api/profile/?{0}'.format(query_string))
            profile_list = api_profile_list.json()
        #profile_list = profile_filter.qs
        context = {'profile_list': profile_list, "profile_filter": profile_filter}
        return render(request, 'pages/profile/profile-list.html', context=context)
    else:
        return redirect('/login/')


# _________ 👥 1.2 Profile Detail  📖 _________________
def profileDetail(request, pk):
    if request.user.is_authenticated:
        # profile detail
        api_profile_detail = requests.get('http://127.0.0.1:8000/api/profile/{0}/'.format(pk))
        profile_detail = api_profile_detail.json()
        #family detail 👨‍👩‍👧‍👧
        api_family_detail = requests.get('http://127.0.0.1:8000/api/profile/{0}/family/'.format(pk))
        family_detail = api_family_detail.json()
        #leave detail ✈️
        api_leave_detail = requests.get('http://127.0.0.1:8000/api/profile/{0}/leave/'.format(pk))
        leave_detail = api_leave_detail.json()

        context = {'profile_detail': profile_detail, 'leave_detail': leave_detail, 'family_detail': family_detail}
        return render(request, 'pages/profile/profile-detail.html', context=context)
    else:
        return redirect('/login/')

# _________ 👥 1.3 Profile Add  ➕ _________________
def profileAdd(request):
    if request.user.is_authenticated:
        # If time: Post data via rest api....
        form = ProfileForm()
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/profile/')
        context = {'form': form,}
        return render(request, "pages/profile/profile-add.html", context=context)
    else:
        return redirect('/login/')

# _________ 👥 1.4 Profile Edit ✏️ _________________
def profileEdit(request, pk):
    if request.user.is_authenticated:
        profile_detail = Profile.objects.get(id=pk)
        form = ProfileForm(instance=profile_detail)
        familymembers = FamilyMemberFormSet(instance=profile_detail)
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES,  instance=profile_detail)
            familymembers = FamilyMemberFormSet(request.POST, request.FILES,  instance=profile_detail)
            if form.is_valid() and familymembers.is_valid():
                familymembers.save()
                form.save()
                return redirect('/profile/')
        # note if anything goes south, user else to put out form for family members
        context = {'form': form,  'familymembers': familymembers, 'profile_detail': profile_detail}
        return render(request, "pages/profile/profile-edit.html", context=context)
    else:
        return redirect('/login/')

# _________ 👥 1.5 Profile Delete ❌ _________________
def profileDelete(request, pk):
    if request.user.is_authenticated:
        api_profile_detail = requests.get('http://127.0.0.1:8000/api/profile/{0}/'.format(pk))
        profile_detail = api_profile_detail.json()
        if request.method == "POST":
            requests.delete('http://127.0.0.1:8000/api/profile/{0}/delete/'.format(pk))
            return redirect('/profile/')
        context = {'profile_detail': profile_detail}
        return render(request, 'pages/profile/profile-delete.html', context=context)
    else:
        return redirect('/login/')



############## 2. LEAVE ✈️ ###################
# 1. Leave List 
# 2. Leave Detail 
# 3. leave Add 
# 4. Leave Edit 
# 5. Leave Delete 

# _________ ✈️ 2.1 Leave List 📃 _________________
# _________ ✈️ 2.2 Leave Detail 📖 _________________
def leaveList(request):
    if request.user.is_authenticated:
        api_leave_list = requests.get('http://127.0.0.1:8000/api/leave/')
        leave_list = api_leave_list.json()
        api_profile_list = requests.get('http://127.0.0.1:8000/api/profile/')
        profile_list = api_profile_list.json()
        leave_filter = LeaveFilter()
        if request.method == 'GET':
            query_string = request.META['QUERY_STRING']
            api_leave_list = requests.get('http://127.0.0.1:8000/api/leave/?{0}'.format(query_string))
            leave_list = api_leave_list.json()
        context = {'leave_list': leave_list, 'profile_list': profile_list, 'leave_filter': leave_filter}
        return render(request, 'pages/leave/leave-list.html', context=context)
    else:
        return redirect('/login/')


# _________ ✈️ 2.3 Leave Add ➕_________________
def leaveAdd(request):
    if request.user.is_authenticated:
        form = LeaveForm()
        if request.method == "POST":
            form = LeaveForm(request.POST or None)
            if form.is_valid():
                #form.save()
                form_cleaned_data = form.cleaned_data
                form_cleaned_data['profile'] = form_cleaned_data['profile'].id
                requests.post('http://127.0.0.1:8000/api/leave/add/', data=form_cleaned_data)
                return redirect('/leave/')
            else:
                messages.error(request, 'Error! Please correct the errors in the form')
        context = {'form': form,}
        return render(request, 'pages/leave/leave-add.html', context=context)
    else:
        return redirect('/login/')

# _________ ✈️ 2.4 Leave Edit ✏️ _________________
def leaveEdit(request, pk):
    if request.user.is_authenticated:
        leave_list = Leave.objects.get(id=pk)
        form = LeaveForm(instance=leave_list)
        if request.method == "POST":
            form = LeaveForm(request.POST or None, instance=leave_list)
            if form.is_valid():
                #form.save()
                form_cleaned_data = form.cleaned_data
                form_cleaned_data['profile'] = form_cleaned_data['profile'].id
                requests.post('http://127.0.0.1:8000/api/leave/{0}/edit/'.format(pk), data=form_cleaned_data)
                return redirect('/leave/')
            else:
                messages.error(request, 'Error! Please correct the errors in the form')
        context = {'form': form}
        return render(request, "pages/leave/leave-edit.html", context=context)
    else:
        return redirect('/login/')

# _________ ✈️ 2.5 Leave Delete ❌ _________________
def leaveDelete(request, pk):
    if request.user.is_authenticated:
        api_leave_detail = requests.get('http://127.0.0.1:8000/api/leave/{0}/'.format(pk))
        leave_detail = api_leave_detail.json()
        if request.method == "POST":
            requests.delete('http://127.0.0.1:8000/api/leave/{0}/delete/'.format(pk))
            return redirect('/leave/')
        context = {'leave_detail': leave_detail}
        return render(request, 'pages/leave/leave-delete.html', context=context)
    else:
        return redirect('/login/')





############## 3. SALARY 💰 ###################
def salaryList(request):
    if request.user.is_authenticated:
        api_profile_list = requests.get('http://127.0.0.1:8000/api/profile/')
        profile_list = api_profile_list.json()
        profile_filter = ProfileFilter()
        if request.method == 'GET':
            query_string = request.META['QUERY_STRING']
            api_profile_list = requests.get('http://127.0.0.1:8000/api/profile/?{0}'.format(query_string))
            profile_list = api_profile_list.json()
        context = {'profile_list': profile_list, 'profile_filter':profile_filter}
        return render(request, 'pages/salary/salary-list.html', context=context)
    else:
        return redirect('/login/')