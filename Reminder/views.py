from django.shortcuts import render

# Create your views here.


from django.core.mail import send_mail
from django.core.mail import EmailMessage


def sendMail(request):
	email = EmailMessage('jhhh', 'hihihi', to=['connectevery1@gmail.com'])
	email.send()