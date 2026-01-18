from django.http import HttpResponse

def home():
    return HttpResponse("<h1>Welcome to the To-Do Application</h1>")