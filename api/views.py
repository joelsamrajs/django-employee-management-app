from functools import partial
from requests import request
from pages.models import Profile, FamilyMember, Leave
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LeaveSerializer, ProfileSerializer, FamilyMemberSerializer
from .filters import *

@api_view(['GET'])
def home(request):
    urls = {
        'list': 'list',
        'info': 'info',
        'create': 'create',
        'update': 'update',
        'delete': 'delete',
    }
    return Response(urls)

############## 1. PROFILE ๐ฅ ###################
# 1. Profile List 
# 2. Profile Detail 
# 3. Profile Family  
# 4. Profile Leave  
# 5. Profile Delete 


# _________ ๐ฅ 1.1 Profile List ๐ _________________
@api_view(['GET'])
def profileList(request):
    profile_list = Profile.objects.all() 
    profile_filter = ProfileFilter(request.GET, queryset=profile_list)
    profile_list = profile_filter.qs
    serializer = ProfileSerializer(profile_list, many=True, allow_null = True)
    return Response(serializer.data)

# _________ ๐ฅ 1.2 Profile Detail  ๐ _________________
@api_view(['GET'])
def profileDetail(request, pk):
    profile_detail = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile_detail, many=False)
    return Response(serializer.data)
    

# _________ ๐ฅ 1.3 Profile Family ๐จโ๐ฉโ๐งโ๐ง _________________
@api_view(['GET'])
def profileFamily(request, pk):
    family_list = FamilyMember.objects.filter(profile=pk)
    serializer = FamilyMemberSerializer(family_list, many=True)
    return Response(serializer.data)

# _________ ๐ฅ 1.4 Profile Leave โ๏ธ _________________
@api_view(['GET'])
def profileLeave(request, pk):
    leave_list = Leave.objects.filter(profile=pk)
    serializer = LeaveSerializer(leave_list, many=True)
    return Response(serializer.data)


# _________ ๐ฅ 1. Profile Delete โ _________________
@api_view(['DELETE'])
def profileDelete(request, pk):
        profile_detail = Profile.objects.get(id=pk)
        family_list = FamilyMember.objects.filter(profile=pk)
        family_list.delete()
        profile_detail.delete() 
        return Response("Profile deleted")
      
           




############## 2. LEAVE โ๏ธ ###################
# 1. Leave List 
# 2. Leave Detail 
# 3. leave Add 
# 4. Leave Edit 
# 5. Leave Delete 

# _________ โ๏ธ 2.1 Leave List ๐ _________________
@api_view(['GET'])
def leaveList(request):
     
        leave_list = Leave.objects.all()
        leave_filter = LeaveFilter(request.GET, queryset=leave_list)
        leave_list = leave_filter.qs
        serializer = LeaveSerializer(leave_list, many=True)
        return Response(serializer.data)
      
           

# _________ โ๏ธ 2.2 Leave Detail ๐ _________________
@api_view(['GET'])
def leaveDetail(request, pk):
        leave_detail = Leave.objects.get(id=pk)
        serializer = LeaveSerializer(leave_detail, many=False)
        return Response(serializer.data)
      
           

# _________ โ๏ธ 2.3 Leave Add โ_________________
@api_view(['POST'])
def leaveAdd(request):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
      
           

# _________ โ๏ธ 2.4 Leave Edit โ๏ธ _________________
@api_view(['POST'])
def leaveEdit(request, pk):
        leave_list = Leave.objects.get(id=pk)
        serializer = LeaveSerializer(instance=leave_list, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
      
           

# _________ โ๏ธ 2.5 Leave Delete โ _________________
@api_view(['DELETE'])
def leaveDelete(request, pk):
        leave_detail = Leave.objects.get(id=pk)
        leave_detail.delete()
        return Response("Leave deleted")
      
           

