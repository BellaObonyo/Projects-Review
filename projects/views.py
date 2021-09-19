from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Project
from django.core.exceptions import ObjectDoesNotExist
from .email import *
from django.contrib import messages
from .forms import *

# Create your views here.
def home(requst):
  return render(requst, 'index.html')

# def services(requst):
#   return render(requst, 'services.html')

# def contact(request):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     message = request.POST.get('message')
#     if request.method == 'POST':
#       contact_form = ContactForm(request.POST)
#       if contact_form.is_valid():
#         contact_form.save()
#         send_contact_email(name, email)
#         data = {'success': 'Thank you for contacting me, I will get back to you shortly'}
#         messages.info(request, f"Message submitted successfully")
#     else:
#       contact_form = ContactForm()
#     return render(request,'contact.html',{'contact_form':contact_form})

# def about(requst):
#   return render(requst, 'about.html')

# def portfolio(request):
#   projects = Project.objects.all().order_by('-published_on')
#   return render(request, 'projects.html', {'projects':projects})

# def detail(request,portfolio_id):
#   try:
#     portfolio = get_object_or_404(Project, pk = portfolio_id)
#   except ObjectDoesNotExist:
#     raise Http404()
#   return render(request, 'portfolio.html', {'portfolio':portfolio})

# def search_portfolio(request):
#   if 'project' in request.GET and request.GET["project"]:
#     search_term = request.GET.get("project")
#     searched_projects = Project.search_project_title(search_term)
#     message = f"{search_term}"

#     return render(request,'search.html', {"message":message,"projects":searched_projects})

#   else:
#     message = "You haven't searched for any term"
#     return render(request,'search.html',{"message":message})