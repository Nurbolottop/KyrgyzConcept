from django.shortcuts import render

#my imports
from apps.index.models import Settings
from apps.jobs.models import Jobs,Category
# Create your views here.

def index(request):
    jobs = Jobs.objects.all()
    category = Category.objects.all()
    
    setting = Settings.objects.latest('id')
    return render(request, "base/index.html", locals())

def about(request):
    setting = Settings.objects.latest("id")
    return render(request, "base/about.html", locals())

def contact(request):
    setting = Settings.objects.latest("id")
    return render(request, "base/contact.html", locals())