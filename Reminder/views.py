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
	print data
	return render(request,"user_list.html",{"list_array" : data})




@csrf_exempt
def send_mails(request):

	email = EmailMessage('jhhh', 'hihihi', to=['connectevery1@gmail.com'])
	email.send()

	return render(request,"mails.html",{})