from django.shortcuts import render
from mainapp.models import Skill,idos

# Create your views here.
def index(reuests):
    skilldic={}
    for i in Skill.objects.values():
        skilldic[i["skill"]]=i["level"]
    context={"skillist":skilldic,"idos":idos.objects.all()}
    return render(reuests,"index.html",context=context)
