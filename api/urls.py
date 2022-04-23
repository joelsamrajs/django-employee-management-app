from django.urls import path
from . import views

urlpatterns = [
    ############## 1. PROFILE 👥 ###################
    # 1. Profile List 
    # 2. Profile Detail 
    # 3. Profile Family  
    # 3. Profile Leave  
    # 4. Profile Delete 
    path('profile/', views.profileList, name='profile-list-api'),
    path('profile/<str:pk>/', views.profileDetail, name='profile-detail-api'),
    path('profile/<str:pk>/family/', views.profileFamily, name='profile-family-api'),
    path('profile/<str:pk>/leave/', views.profileLeave, name='profile-leave-api'),
    path('profile/<str:pk>/delete/', views.profileDelete, name='profile-delete-api'),

    ############## 2. LEAVE ✈️ ###################
    # 1. Leave List 
    # 2. Leave Detail 
    # 3. leave Add 
    # 4. Leave Edit 
    # 5. Leave Delete 
    # 6. Leave Filter Profile 
    path('leave/', views.leaveList),
    path('leave/<int:pk>/', views.leaveDetail),
    path('leave/add/', views.leaveAdd),
    path('leave/<int:pk>/edit/', views.leaveEdit),
    path('leave/<str:pk>/delete/', views.leaveDelete),
    

    

    
   
]