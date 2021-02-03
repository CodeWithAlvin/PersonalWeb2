from django.shortcuts import render

# Create your views here.
def index(reuests):
    return render(reuests,"index.html")

