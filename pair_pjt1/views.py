from importlib.resources import contents
from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    reviews =Review.objects.all()

    context={
        'Review':  reviews
    }

    return render(request,'index.html',context)

def create(request):


    return render(request, "create.html")

def send(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    created_at = request.GET.get('created_at')
    update_ad = request.GET.get('update_ad')

    Review.objects.create(
        title = title,
        content = content,
        created_at = created_at,
        update_ad = update_ad,

    )

    return redirect('pair:index')


def detail(request,pk):
    pk= Review.objects.get(id=pk)

    context={
        'id':pk
    }

    return render(request,'detail.html',context)

def delete(request, pk):
    pk= Review.objects.get(id=pk)
    pk.delete()

    return redirect('pair:index')

def edit(request, pk):
    pk= Review.objects.get(id=pk)

    context = {
        'pk': pk
    }

    return render(request, 'edit.html', context)

def update(request, pk):
    pk= Review.objects.get(id=pk)

    title = request.GET.get('title')
    content = request.GET.get('content')

    pk.title = title
    pk.content = content

    pk.save()

    return redirect('pair:detail', pk.pk)
