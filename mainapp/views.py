from django.shortcuts import render,redirect,reverse
from mainapp.models import Skill, idos, About, Contact
from django.contrib import messages
from datetime import datetime
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
        messages.success(request, "Your Request has been submited")
        return redirect(reverse('index'))
    messages.success(request, "An Error Occured Please Try Again")
    return redirect(reverse('index'))
