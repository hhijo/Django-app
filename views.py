from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name='index.html')
def about(request):
    return render(request,template_name='about.html')
def contacts(request):
    return render(request,template_name='contact.html')
def services(request):
    return render(request,template_name='services.html')
def blog(request):
    return render(request,template_name='blog.html')
