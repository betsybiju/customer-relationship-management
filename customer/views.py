from django.shortcuts import render,redirect
from django.db import models
from .models import customer,feedback
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

def home(request):
	return render(request,'customer.html')

def loginpage(request):
	return render(request,'login1.html')

def aboutus(request):
	return render(request,'about.html')

def changepass(request):
	fm=PasswordChangeForm(user=request.user)
	return render(request,'password.html',{'form':fm})

def customerpage(request):
	dtls=customer.objects.all()
	return render(request,"custom.html",{'dtls':dtls})

def display(request):
	dtls=feedback.objects.all()
	return render(request,"displayfeed.html",{'dtls':dtls})

def adding(request):
	return render(request,'add.html')

def feeding(request):
	return render(request,'feed.html')

def editing(request):
	return render(request,'edit.html')

def feedback1(request):
	dic={}
	flag=0
	try:
		if request.method=="POST":
			N=request.POST["name"]
			E=request.POST["email"]
			P=request.POST["phone"]
			M=request.POST["message"]
			dtls=feedback.objects.all()
			data=feedback(name=N,email=E,phone=P,msg=M)
			data.save()
			return redirect('display')
	except Exception as e:
		print(e)
		dic["msg0"]="can't be added"
		return render(request,"feed.html",dic)

def addcustomer(request):
	dic={}
	flag=0
	try:
		if request.method=="POST":
			N=request.POST["name"]
			A=request.POST["address"]
			E=request.POST["email"]
			P=request.POST["phone"]
			dtls=customer.objects.all()
			data=customer(name=N,address=A,email=E,phone=P)
			data.save()
			return redirect('loginpage')
	except Exception as e:
		print(e)
		dic["msg0"]="can't be added"
		return render(request,"add.html",dic)


def loginview(request):
	username=request.POST['username']
	password=request.POST['password']
	user=authenticate(request,username=username,password=password)
	if user is not None:
		login(request,user)
		return redirect('loginpage')
	else:
		return render(request,'login.html')


def sign_up(request):
	dic={}
	form=UserCreationForm(request.POST)
	if request.method=="POST":
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(request,username=username,password=password)
			login(request,user)
			return redirect('login')
	else:
		form=UserCreationForm()
	return render(request,'registration/sign_up.html',{'form':form})

def updatename(request):
	dic={}
	try:
		Name=request.POST['name']
		Newname=request.POST['newname']
		dtls=customer.objects.get(name=Name)
		if Name in dtls.name:
			dtls.name=Newname
			dtls.save()
			dic["msg0"]="name updated"
			return render(request,"edit.html",dic)
		else:
			dic["msg1"]="can't found the name"
			return render(request,"edit.html",dic)
	except Exception as e:
		print(e)
		dic["msg2"]="name cannot be added"
		return render(request,"edit.html",dic)

def updatephone(request):
	dic={}
	try:
		Name=request.POST['name']
		Newnum=request.POST['newnum']
		dtls=customer.objects.get(name=Name)
		if Name in dtls.name:
			dtls.phone=Newnum
			dtls.save()
			dic["msg3"]="number updated"
			return render(request,"edit.html",dic)
		else:
			dic["msg4"]="can't found the name"
			return render(request,"edit.html",dic)
	except Exception as e:
		print(e)
		dic["msg5"]="contact cannot be added"
		return render(request,"edit.html",dic)

def updateaddress(request):
	dic={}
	try:
		Name=request.POST['name']
		Newaddress=request.POST['newaddress']
		dtls=customer.objects.get(name=Name)
		if Name in dtls.name:
			dtls.address=Newaddress
			dtls.save()
			dic["msg6"]="address updated"
			return render(request,"edit.html",dic)
		else:
			dic["msg7"]="can't found the name"
			return render(request,"edit.html",dic)
	except Exception as e:
		print(e)
		dic["msg8"]="address cannot be added"
		return render(request,"edit.html",dic)

def updateemail(request):
	dic={}
	try:
		Name=request.POST['name']
		Newemail=request.POST['newemail']
		dtls=customer.objects.get(name=Name)
		if Name in dtls.name:
			dtls.email=Newemail
			dtls.save()
			dic["msg9"]="email updated"
			return render(request,"edit.html",dic)
		else:
			dic["msg10"]="can't found the name"
			return render(request,"edit.html",dic)
	except Exception as e:
		print(e)
		dic["msg11"]="email cannot be added"
		return render(request,"edit.html",dic)
# Create your views here.
