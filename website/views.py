from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .forms import AddRecordForm
from .models import record

def home(request):

	records=record.objects.all()

	if request.method=='POST':

		username=request.POST['username']
		password=request.POST['password']

		user=authenticate(request,username=username, password=password)

		if user is not None: 

			login(request,user)
			messages.success(request, "You have been Logged In")
			return redirect('home')

		else:
			messages.success(request, "There was an error ")
			return redirect('home')

	else:

		return render(request,'home.html',{'records':records})


def check(request):
	return redirect('home')

def login_user(request):
	return redirect('home')

def logout_user(request):
	logout(request)
	messages.success(request,'Successfully Logged Out')
	return redirect('home')


def register_user(request):
	return render(request, 'register.html' , {} )

def customer_record(request,pk):
	if request.user.is_authenticated:

		customer_record=record.objects.get(id=pk)

		return render(request, 'record.html', {'customer_record':customer_record})

	else:
		messages.success(request,'You Must be Logged in ')
		return redirect('home')

def delete_customer_record(request,pk):
	if request.user.is_authenticated:

		customer_record=record.objects.get(id=pk)
		customer_record.delete()
		messages.success(request,'Deleted Successfully...')
		return redirect('home')
	else:
		messages.success(request,'You Must be Logged in ')
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)

	if request.user.is_authenticated:
		if request.method=='POST':
			if form.is_valid:
				add_record=form.save()
				messages.success(request,'Success...')
				return redirect('home')
		return render(request,'add_record.html',{'form':form})
	else:
		messages.success(request,'You must be Logged in ... ')
		return redirect('home')



def update_record(request,pk):
	if request.user.is_authenticated:
		current_record=record.objects.get(id=pk)
		form= AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request,'Success ... ')

			return redirect('home')
		return render(request, 'update_record.html', {'form':form, 'customer_record_id':current_record.id})
	else:
		messages.success(request,'Please Loggin ...')
		return redirect('home')

























