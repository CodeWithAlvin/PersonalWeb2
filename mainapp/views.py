from django.shortcuts import render
from mainapp.models import Skill

# Create your views here.
def index(reuests):
    skilldic={}
    for i in Skill.objects.values():
        skilldic[i["skill"]]=i["level"]
    return render(reuests,"index.html",context={"skillist":skilldic})
