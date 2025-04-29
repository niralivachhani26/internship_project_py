from django.shortcuts import render

def index(request):
    banners = [
        {'image_url': 'images/banner1.png'},
        {'image_url': 'images/banner2.png'},
        {'image_url': 'images/banner3.png'},
    ]
    return render(request, 'index.html', {'banners': banners})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def clients(request):
    return render(request, 'clients.html')

def blogs(request):
    return render(request, 'blogs.html')

def careers(request):
    return render(request, 'careers.html')

def contact(request):
    return render(request, 'contact.html')