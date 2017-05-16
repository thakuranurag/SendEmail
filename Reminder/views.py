from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import UserData
import json
# Create your views here.


from django.core.mail import send_mail
from django.core.mail import EmailMessage

@csrf_exempt
def add_details(request):
	if request.method=='GET':
		return render(request,"add_details.html",{})

	else:
		name = request.POST.get("user_name")
		phone = request.POST.get("phone")
		email = request.POST.get("email")
		date = request.POST.get("date")

		UserData.objects.create(name=name,phone=phone,email=email,date=date)

		return render(request,"add_details.html")

@csrf_exempt
def show_details(request):

	if request.method=='GET':
		data = UserData.objects.all()
		list_array = []
		for x in data:
			list_object = {}
			list_object["name"] = x.name
			list_object["phone"]=x.phone
			list_object["email"]=x.email
			list_object["date"] = str(x.date)
			list_array.append(list_object)

		data = json.dumps(list_array)

		return render(request,"user_list.html",{"list_array" : data})

	if request.method=='POST':
		start_date = request.POST.get("start")
		deadline = request.POST.get("deadline")
		print start_date,deadline

		allData = UserData.objects.filter(date__range=[str(start_date),str(deadline)])
		print allData

		list_array = []
		for x in allData:
			list_object = {}
			list_object["name"] =x.name
			list_object["phone"]=x.phone
			list_object["email"]=x.email
			list_object["date"] = str(x.date)
			list_array.append(list_object)

		allData = json.dumps(list_array)
		
		return render(request,"user_list.html",{"list_array" : allData})




@csrf_exempt
def send_mails(request):


	mails = request.GET.get("demo")

	print mails

	newData = json.loads(mails)

	

	print newData[0]
	
	for x in newData:
		email = EmailMessage('Hello Bro', 'Anurag here', to=[x])
		email.send()

	return render(request,"mails.html",{})