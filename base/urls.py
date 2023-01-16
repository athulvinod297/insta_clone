from django.urls import path
from .views import ProfileList,ProfileDetail,ProfileUpdate,CustomLogin,RegisterPage,UserProfile,AddImage
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm

urlpatterns=[
    path('login/',CustomLogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('home/',ProfileList.as_view(),name='home'),
    path('profile/<str:pk>',ProfileDetail.as_view(),name='profile'),
    path('profile-update/<str:pk>',ProfileUpdate.as_view(),name='profile-update'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('addimage/',AddImage.as_view(),name='addimage'),
    path('userprofile/',UserProfile.as_view(),name='userprofile')

] 