from django.shortcuts import render, redirect
from .models import Products, Category
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    question = Products.objects.all()
    category = Category.objects.all()
    data = {'category' : category}
    return render(request, 'template.html', data)

def category(request, id):
    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user)

def products(request, id):
    products_user = Products.objects.get(pk=id)
    inscryption = "<h1>" +  str(products_user) + "</h1>" + \
        "<p></p>" +  str(products_user.descryption)  + "</p>" + \
        "<p>" +  str(products_user.price) + "</p>"
    return HttpResponse(inscryption)

def SearchPage(request):
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