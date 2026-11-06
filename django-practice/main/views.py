from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет, это мой первый сайт на Django!")