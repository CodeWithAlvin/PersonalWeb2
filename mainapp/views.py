from django.shortcuts import render,redirect,reverse
from mainapp.models import Skill, idos, About, Contact
from django.contrib import messages
from datetime import datetime
import smtplib,os
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
        try:
            send_mail(name,mail,desc)
        except:
            return render(request,'err.html')
        return redirect(reverse('index'))
    return render(request,'err.html')

def send_mail(name,email,desc):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    s.login(os.environ.get("mail"), os.environ.get("passkey"))
    message=f"""
    <h1>Contact Request from {name}</h1>
    <br>
    <h3>Email : {email}</h3>
    <br>
    <h2> {name} said </h2>
    <br>
    <p>{desc}</p>
    """
    server.sendmail(os.environ.get("mail"), "sainialvin@gmail.com" , message)
    server.quit()