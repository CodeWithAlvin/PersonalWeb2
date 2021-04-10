from django.shortcuts import render,redirect,reverse
from mainapp.models import Skill, idos, About, Contact
from django.contrib import messages
from datetime import datetime
import os
from django.core.mail import send_mail 

# Create your views here.

def index(reuests):
    skilldic = {}
    for i in Skill.objects.values():
        skilldic[i["skill"]] = i["level"]
    context = {"skillist": skilldic, "idos": idos.objects.all(
    ), "about": About.objects.values()[0].get("about")}
    return render(reuests, "index.html", context=context)


def submit(request):
    if(request.method == "POST"):
        name = request.POST.get("name")
        mail = request.POST.get("mail")
        desc = request.POST.get("desc")
        data = Contact(name=name, email=mail, desc=desc, date=datetime.now())
        data.save() 
        sendContact(name,mail,desc)
        return redirect(reverse('index'))
    return render(request,'err.html')

def sendContact(name,email,desc):
    mail_subject=f"Contact Request from {name}"
    message=f"""
    Email : {email}\n
    {name} said\n
    {desc}
    """
    send_mail(mail_subject, message, os.environ.get('mail'), ["codewithalvin@gmail.com"], 
              fail_silently=False)