from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import Contact
# Create your views here.

def index_view(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        form = Contact.objects.create(name=name, email=email, phone=phone, message=message)
        form.save()
    
    return render(request, 'index.html')
# class IndexView(TemplateView, FormView):
    
#     template_name = "index.html"
#     form_class = ContactForm

# class JournalView(TemplateView):
#     template_name = "journal.html"
