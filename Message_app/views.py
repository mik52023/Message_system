from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from . import WebServices
from django.core import serializers

# Create your views here.

# all the functions that handle the requests and responds for each url

@require_POST
def create_message_view(request):
 try:
    sender=request.POST["sender"]
    reciever=request.POST["reciever"]
    subject=request.POST["subject"]
    content=request.POST["content"]

    message=WebServices.create_message(sender,reciever,subject,content)

    if(message!=None):
        send_data={"info":"message was sent"}
    else:
        send_data={"info":"message could not be sent"}

    return JsonResponse(send_data)

 except  Exception as e:
     send_data = {"info": "error has occurred",
                  "error": e.args}
     return JsonResponse(send_data)

@require_GET
def read_message_view(request):
    try:
        user=request.GET["user"]
        id=request.GET["id"]

        message=WebServices.read_message(id,user)
        data=model_to_dict(message,exclude=('id'))
        send_data={'data':data}
        return JsonResponse(send_data)
    except  Exception as e:
         send_data = {"info": "error has occurred",
                      "error":e.args}
         return JsonResponse(send_data)

@require_GET
def delete_message_view(request):
    try:
        user=request.GET["user"]
        id=request.GET["id"]

        message=WebServices.get_message(id)
        WebServices.delete_message(user,message)
        send_data = {"info": "message was deleted"}
        return JsonResponse(send_data)
    except  Exception as e:
         send_data = {"info": "error has occurred",
                      "error":e.args}
         return JsonResponse(send_data)


@require_GET
def get_messages_by_user_view(request):
    try:
        user=request.GET["user"]
        data=[]
        messages=WebServices.get_messages_by_user(user)
        for message in messages:
            data.append(model_to_dict(message,exclude=('id')))
        send_data={'data':data}
        return JsonResponse(send_data)
    except  Exception as e:
         send_data = {"info": "error has occurred",
                      "error":e.args}
         return JsonResponse(send_data)


@require_GET
def get_unread_messages_by_user_view(request):
    try:
        user = request.GET["user"]
        data = []
        messages = WebServices.get_unread_messages_by_user(user)
        for message in messages:
            data.append(model_to_dict(message, exclude=('id')))
        send_data = {'data': data}
        return JsonResponse(send_data)
    except  Exception as e:
        send_data = {"info": "error has occurred",
                     "error": e.args}
        return JsonResponse(send_data)
