from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm,Query
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import stock
from app.models import stock



# query Form
def query(request):
 if request.method == "POST":
  fm = Query(request.POST)
  if fm.is_valid():
   messages.success(request, 'Query Form Submitted Successfully !!') 
   fm.save()
 else: 
  fm = Query()
 return render(request, 'query.html', {'form':fm})

# home page
def index(request):
 if request.user.is_authenticated: 
  st = stock.objects.all()
  return render(request, 'index.html', {'st':st})
 else:
  return HttpResponseRedirect('/login/') 

# Signup View Function
def sign_up(request):
 if request.method == "POST":
  fm = SignUpForm(request.POST)
  if fm.is_valid():
   messages.success(request, 'Account Created Successfully !!') 
   fm.save()
 else: 
  fm = SignUpForm()
 return render(request, 'signup.html', {'form':fm})

# Login View Function
def user_login(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
        uname = fm.cleaned_data['username']
        upass = fm.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, 'Logged in successfully !!')
          return HttpResponseRedirect('/profile/')
    else: 
      fm = AuthenticationForm()
    return render(request, 'userlogin.html', {'form':fm})
  else:
    return HttpResponseRedirect('/profile/')

# Profile
def user_profile(request):
  if request.user.is_authenticated:
    return render(request, 'profile.html', {'name': request.user})
  else:
    return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/login/')

# Search
def search(request):
  if request.user.is_authenticated:
    search = request.GET['search']
    sn = stock.objects.filter(stockname__icontains=search)
    return render(request,'search.html',{'sn':sn}) 
  else:
    return HttpResponseRedirect('/login/') 


# for details
def desc(request,slug):
  desc = stock.objects.get(dslug=slug)
  return render(request,'desc.html',{'desc':desc}) 




