from django.shortcuts import render,redirect
from .models import *

# Create your views here.

from .forms import PostForm




def homepage(r):
    data = {}
    data['generous'] = Generous.objects.all()
    data['create'] = Books.objects.all()
    
    return render(r,"home.html",data)


def insert(r):
    if r.method == "POST":
        p = PostForm(r.POST,r.FILES)
        if p.is_valid():
            p.save()
        return redirect(homepage)

    return render(r,"insert.html",{"form":PostForm})


def viewPost(r,cat_id):
    data = {}
    data['generous'] = Generous.objects.all()
    data['create'] = Books.objects.filter(generous=cat_id)
    return render(r,"home.html",data)

def search(r):
    search = r.GET.get("search")
    data = {
        "generous":Generous.objects.all(), 
        "create":Books.objects.filter(title__icontains=search),
        }
    return render(r, "home.html",data)
  

def singlePost(r,post_id):
    data = {}
    data['generous'] = Generous.objects.all()
    data['show'] = Books.objects.get(pk=post_id)
   
    data['create'] = Books.objects.exclude(pk=post_id)
    return render(r,"view.html",data)

