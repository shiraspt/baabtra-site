from django.shortcuts import render

# Create your views here.
def master (request):
    return render (request, "babtra_master.html")

def aboutus (request):
    return render (request, "aboutus.html")

def placement (request):
    return render (request, "placement.html")

def blog (request):
    return render (request, "blog.html")

def gallery (request):
    return render (request, "gallery.html")

def home (request):
    return render (request, "home.html")

def contact (request):
    return render (request, "contact.html")