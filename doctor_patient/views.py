from django.shortcuts import render, redirect
from .models import Doctor

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    doctors = Doctor.objects.all()
    return render(request, 'dashboard.html', {'doctors':doctors})

def view(request, id):
    pass

def add(request):
    Doctor.objects.create(name=request.POST.get("name"), dob=request.POST.get("dob"), gender=request.POST.get("gender"), email=request.POST.get("email"), mobile=request.POST.get("mobile"),
                          state=request.POST.get("state"), city=request.POST.get("city"), nationality=request.POST.get("nationality"), zipcode=request.POST.get("zipcode"), 
                          bio=request.POST.get("bio"), imcid=request.POST.get("imcid"), regno=request.POST.get("regno"), specialization=request.POST.get("specialization"), shift=request.POST.get("shift"), 
                          degree=request.POST.get("degree"), online_profile_link=request.POST.get("online_profile_link"), yoe=request.POST.get("yoe"), language=request.POST.get("language"),
                          available=request.POST.get("available"), fees=request.POST.get("fees"))
    return redirect('dashboard')

def delete(request, id):
    Doctor.objects.filter(id=id).delete()
    return redirect('dashboard')

def update(request, id):
    Doctor.objects.update(id=id, name=request.POST.get("name"), dob=request.POST.get("dob"), gender=request.POST.get("gender"), email=request.POST.get("email"), mobile=request.POST.get("mobile"),
                          state=request.POST.get("state"), city=request.POST.get("city"), nationality=request.POST.get("nationality"), zipcode=request.POST.get("zipcode"), 
                          bio=request.POST.get("bio"), imcid=request.POST.get("imcid"), regno=request.POST.get("regno"), specialization=request.POST.get("specialization"), shift=request.POST.get("shift"), 
                          degree=request.POST.get("degree"), online_profile_link=request.POST.get("online_profile_link"), yoe=request.POST.get("yoe"), language=request.POST.get("language"),
                          available=request.POST.get("available"), fees=request.POST.get("fees"))
    return redirect('dashboard')