from django.shortcuts import render
from mainapp.models import Skill

# Create your views here.
def index(reuests):
    skilllist={}
    for i in Skill.objects.values():
        skilllist['']
    return render(reuests,"index.html",context={"skillist":skillist})
