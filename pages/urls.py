from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),


    ############## 1. PROFILE 👥 ###################
    # 1. Profile List 
    # 2. Profile Detail 
    # 3. Profile Add  
    # 4. Profile Edit 
    # 5. Profile Delete
    path('profile/', views.profileList, name='profile-list'),
    path('profile/<int:pk>/', views.profileDetail, name='profile-detail'),
    path('profile/add/', views.profileAdd, name='profile-add'),
    path('profile/<int:pk>/edit/', views.profileEdit, name='profile-edit'),
    path('profile/<int:pk>/delete/', views.profileDelete, name='profile-delete'),

    ############## 2. LEAVE ✈️ ###################
    # 1. Leave List 
    # 2. Leave Detail  (leave detail is combilined in leave list)
    # 3. leave Add 
    # 4. Leave Edit 
    # 5. Leave Delete 
    path('leave/', views.leaveList, name='leave-list'),
    path('leave/add/', views.leaveAdd, name='leave-add'),
    path('leave/<int:pk>/edit/', views.leaveEdit, name='leave-edit'),
    path('leave/<int:pk>/delete/', views.leaveDelete, name='leave-delete'),

    ############## 3. SALARY 💰 ###################
    path('salary/', views.salaryList, name='salary-list'),


    
]