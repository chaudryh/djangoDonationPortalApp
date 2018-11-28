from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm
from .models import User

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'registration/signup.html')

def edit_user(request, id):
    User.objects.filter(id=id).delete()
    return render(request, 'edit_user.html')


def delete_user(request,name):
    User.objects.filter(User,id=id).delete()
    return render(request, 'userManagement.html')

def donation_detail(request, id):
    user = get_object_or_404(User,id=id)
    return render(request, "donation_detail.html", {'user': user})

def user_Management(request):
    users = User.objects.all()
    return render(request, "userManagement.html", {'users': users})

def admintemplate(request):
    return render(request, "AdminTemplate.html")


def donation(request):
    print("in donation")
    if request.method == "POST":
        form = UserForm(request.POST)
        print("form validation")
        if form.is_valid():
            print("creating a user object")
            user = form.save(commit=False)
            user.save()
            print("after save")
            return redirect("donation_detail", id=user.id)
    else:
        print("in else")
        form = UserForm()
        print(form)
        return render(request,"donation.html", {'form': form})
