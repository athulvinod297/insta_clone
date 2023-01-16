from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,CreateView,FormView
from .models import Uploads,Profile
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage,self).form_valid(form)



class CustomLogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class ProfileList(LoginRequiredMixin,ListView):
    model = Profile
    context_object_name = 'profiles'
    
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles']=context['profiles'].exclude(user=self.request.user)
        return context



class ProfileDetail(LoginRequiredMixin,DetailView):
    model = Profile
    context_object_name = 'profiles'

    
   

class ProfileUpdate(LoginRequiredMixin,UpdateView):
    model = Profile
    fields = ['username','email','profile_image']
    success_url = reverse_lazy('userprofile')

class AddImage(LoginRequiredMixin,CreateView):

    template_name = 'base/upload_image.html'
    model = Uploads
    fields = '__all__'
    success_url = reverse_lazy('home')




    


class UserProfile(LoginRequiredMixin,ListView):
    template_name = 'base/user_profile.html'
    model = Profile
    context_object_name = 'profiles'
   

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles']=context['profiles'].get(user=self.request.user)
        return context
