from django.shortcuts import render

# Create your views here.
def index(reuests):
    skillist={"python":90,"html":85,"Javascript":30}
    return render(reuests,"index.html",context={"skillist":skillist})

