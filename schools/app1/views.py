from django.contrib.auth.management.commands.changepassword import UserModel
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.generic import CreateView,ListView,DetailView

from app1.models import School,Student
from app1.forms import SchoolForm,StudentForm

class HomeView(TemplateView):
    template_name="home.html"
from django.urls import reverse_lazy
class AddschoolView(CreateView):
    model=School
    form_class=SchoolForm
    template_name="addschool.html"
    success_url=reverse_lazy('home')

class AddstudentView(CreateView):
    model=Student
    form_class=StudentForm
    template_name="addstudent.html"
    success_url=reverse_lazy('home')

class SchoollistView(ListView):
    model=School
    context_object_name='school'
    template_name="schoollist.html"

class SchooldetailView(DetailView):
    model=School
    context_object_name='school'
    template_name="detail.html"

from app1.forms import RegisterForm
from django.contrib.auth.models import User
class RegisterView(CreateView):
    form_class=RegisterForm
    template_name="register.html"
    model=User
    success_url=reverse_lazy('home')
    def form_valid(self,form):  #in CreateView after validation it will call form_valid() function to save the data.
        f=form.save(commit=False)   #in our class we  redefine the form_valid().so after validation it will call form_valid() inside our class
        password=form.cleaned_data['password'] #here we access the password field from cleaned_data


        f.set_password(password) #To change into encrypted format we use set_password()
        f.save() #then it will save the form object into table User
        return super().form_valid(form) #inorder to redirect into home page we call super().form_valid()

from django.contrib.auth.views import LoginView
class UserLogin(LoginView):
    template_name="login.html"


def user_logout(request):
    logout(request)
    return redirect('home')


from django.contrib.auth import logout
from django.views import View
class User_logout(View):
    def get(self,request):
        logout(request)
        return redirect('home')




