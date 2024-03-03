from django.views.generic import View
from django.http import JsonResponse
from django.views import View
import requests
import json

from urllib3 import Retry
# from django.http import HttpResponse
from . forms import SignupForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import uuid

def profile (request):
    return render(request, 'profile.html')



def index(request):
    if request.user.is_authenticated:
        processors = Processor.objects.all()
        transactions = Transaction.objects.filter(user=request.user)
        
        pending_transactions = 0
        paid_transactions = 0
        total = 0

        for item in transactions:
            total += int(item.amount)

        context = {
            'processors': processors,
            'transactions': transactions,
            'subtotal': pending_transactions,
            'discount': paid_transactions,
            'total': total
        }    

        return render(request, 'index.html', context)
    else:
        return redirect('login') 


def transaction(request,id):
    transactions = Transaction.objects.filter(user=request.user)
    products = Product.objects.all()
    

    context={
        'transactions': transactions,
        'products': products,
        
    }
    return render(request,'transaction.html', context)

def pay(request):
    id= request.POST.get('proc')
    proc = Processor.objects.get(pk=id)
    user = User.objects.get(username=request.user)
    amount= request.POST.get('fee')
    code = str(uuid.uuid4())
    status = request.POST.get('status')
    trans = Transaction()
    if request.method == 'POST':
        trans.processor = proc
        trans.user = user
        trans.confirmation_code = code
        trans.status = status
        trans.amount = amount
        trans.save()
        messages.success(request, "Transaction Successful")
        
    return redirect('index')


def print(request):
	context = {}
	return render(request, 'print.html', context)



def render_to_pdf(template_src, context_dict={}):
    
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
}

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('pdf_template.html', data)
  
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response

def signupform(request):
    reg = SignupForm()
    if request.method == 'POST':
        reg = SignupForm(request.POST)
        if reg.is_valid():
            new = reg.save()
            login(request, new)
            messages.success(request, 'Signup successfull!')
            return redirect('index')
        else:
            messages.warning(request, reg.errors)
            return redirect('signupform')

    context = {
        'reg': reg
    }

    return render (request,'signup.html', context)


def password(request):
    update = PasswordChangeForm(request.user)
    if request.method == 'POST':
        update = PasswordChangeForm(request.user, request.POST)
        if update.is_valid():
            user=update.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password update successful!')
            return redirect('index')
        else:
            messages.error(request, update.errors)
            return redirect('password')

    context = {
        'update': update
    }

    return render(request, 'password.html', context)


def logoutfunc(request):
    logout(request)
    return redirect('login')

def loginfunc(request):  
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            messages.success(request, "Welcome to my task!")
            
            return redirect('index')
        else:
            return redirect('login')
        
    return render (request, 'login.html')





