from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        bookname = request.POST.get('bookname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists() or Book.objects.filter(name=bookname).exists():
                messages.error(request,'UserName or Email or BookName is Already Taken.')
            else:
                user = User.objects.create_user(username = username, email = email, password = password1)
                book = Book.objects.create(user = user, name = bookname)
                user.save()
                book.save()
                return redirect('login')
        else:
            messages.error(request,'Passwords do not Match.')
    return render(request,'MakeOwnBookApp/register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('basePage')
        else:
            messages.error(request,'UserName or Password is Incorrect.')
    return render(request,'MakeOwnBookApp/login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def basePage(request):
    pages = Content.objects.filter(user=request.user).order_by('date')
    book = Book.objects.get(user = request.user)
    context = {'pages':pages,'book':book}
    return render(request,'MakeOwnBookApp/base.html',context)

@login_required(login_url="login")
def mainPage(request,page):
    pages = Content.objects.filter(user=request.user).order_by('date')
    book = Book.objects.get(user = request.user)
    pageno = Content.objects.get(id = page)
    context = {'pages':pages,'book':book,'pageno':pageno}
    return render(request,'MakeOwnBookApp/main.html',context)

@login_required(login_url="login")
def newPage(request):
    pages = Content.objects.filter(user=request.user).order_by('date')
    book = Book.objects.get(user = request.user)
    if request.method == 'POST':
        newtitle = request.POST.get('newtitle')
        newstory = request.POST.get('newstory')
        newpage = Content.objects.create(user=request.user,title=newtitle, story=newstory)
        newpage.save()
        return redirect('basePage')
    context = {'pages':pages,'book':book}
    return render(request,'MakeOwnBookApp/new.html',context)

@login_required(login_url="login")
def deletePage(request,page):
    pagename = Content.objects.get(id=page)
    if request.method == 'POST':
        pagename.delete()
        return redirect('basePage')
    context = {'pagename':pagename}
    return render(request,'MakeOwnBookApp/delete.html',context)

@login_required(login_url="login")
def aboutPage(request):
    details = User.objects.get(id=request.user.id)
    book = Book.objects.get(user = request.user)
    pagecount = Content.objects.filter(user = request.user).count()
    context = {'details':details,'pagecount':pagecount,'book':book}
    return render(request,'MakeOwnBookApp/about.html',context)