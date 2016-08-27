import json

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse

# Create your views here.
def test(request):
    param1 = request.GET.get('param1', '1')
    #param2 = request.GET.get('param2', '2')
    param3 = request.GET.get('param3', '3')

    #param1 = request.GET['param1']
    param2 = request.GET['param2']
    #param3 = request.GET['param3']
    #return HttpResponse("param1: %s, param2: %s, param3: %s" % (param1, param2, param3))


    text = "param1: %s"
    text += "<br>"
    text += "param2: %s"
    text += "<br>"
    text += "param3: %s"
    text += "<br>"

    #print(request.GET)   <QueryDict: {'param1': [''], 'param2': ['']}>
    return HttpResponse(text % (param1, param2, param3))

def login(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario', None)
        clave = request.POST.get('clave', None)

        user = authenticate(username=usuario, password=clave)
        if user is not None:
            # A backend authenticated the credentials
            response = JsonResponse(
                {
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                 }
            )
        else:
            response = HttpResponse(status=401)
    else:
        response = HttpResponse('<!-- Use POST -->')

    return response