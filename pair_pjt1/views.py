from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(requst):

    return render(requst, "create.html")

def send(requst):
    title = requst.GET.get('title')
    content = requst.GET.get('content')
    created_at = requst.GET.get('created_at')
    update_ad = requst.GET.get('update_ad')

    Review.objects.create(
        title = title,
        content = content,
        created_at = created_at,
        update_ad = update_ad,

    )

    return redirect('pair:index')