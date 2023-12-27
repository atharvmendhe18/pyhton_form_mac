from django.shortcuts import render
tasks = ["Django", "Task4", "Task3"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html",{
        "tasks": tasks
    })