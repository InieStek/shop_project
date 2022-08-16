from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Products, Category, Producent


# Create your views here.

def index(request):
    question = Products.objects.all()
    category = Category.objects.all()
    data = {'category' : category, 'question' : question}
    return render(request, 'template.html', data)

def category(request, id):
    category_user = Category.objects.get(pk=id)
    products_user = Products.objects.get(pk=id)
    data = {'category_user': category_user, 'products_user' : products_user}
    return render(request, 'category_products.html', data)

def products(request, id):
    products_user = Products.objects.get(pk=id)
    producent_user = Producent.objects.get(pk=id)
    category = Category.objects.all()
    inscryption = {'products': products, 'products_user' : products_user, 'producent_user' : producent_user, 'category' : category}
    return render(request, 'products.html', inscryption)

def searchPage(request):
    srh = request.GET['query']
    products = Products.objects.filter(name__icontains=srh)
    params = {'products': products, 'search': srh}
    return render(request, 'searchbar.html', params)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})