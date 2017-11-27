from django.shortcuts import render,redirect
from django.http import HttpResponse
from telethon import TelegramClient
import json
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.types import InputChannel
# import Cookie
# from .utils import InteractiveTelegramClient
# from telethon.tl.functions.messages import GetHistoryRequest


def index(request):
    return render (request,"base.html",{})

def genrate_otp(request):
    api_id   = 169722
    api_hash = '    '
    phone    = '+918962141530'
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()
    client.session.try_load_or_create_new(session_user_id= '%s' % client.session.auth_key.key_id)
    if not client.is_user_authorized(): 
        client.sign_in(phone=phone)
        phone_has_code=client._phone_code_hash
        data = {'message':'otp genrated','status':409,'code':phone_has_code}
        return HttpResponse(json.dumps(data),content_type="application/json")
    data = {'message':'Accoutn not creates','status':401}
    return HttpResponse(json.dumps(data),content_type="application/json")

def load_settings(request): 
    otp=request.GET.get('data')
    code=request.GET.get('code')
#     data = {}
    api_id   = 169722
    api_hash = 'b4d4b4374d60a3ba9d7ee84ce010e2b2'
    phone    = '+918962141530'
    client1 = TelegramClient('+918962141530', api_id, api_hash)
    client1.session.try_load_or_create_new(session_user_id='+918962141530')
    client1.connect()
    if otp and code:
            # import pdb; pdb.set_trace()
            me =client1.sign_in(phone='+918962141530', code=otp, phone_code_hash=code)

    data = {'message':'Accoutn not creates','status':401}
    return HttpResponse(json.dumps(data),content_type="application/json")
    
def send_message(request): 
    message=request.GET.get('data')
    api_id   = 169722
    api_hash = 'b4d4b4374d60a3ba9d7ee84ce010e2b2'
    phone    = '+918962141530'
    client1 = TelegramClient('+918962141530', api_id, api_hash)
    client1.session.try_load_or_create_new(session_user_id='+918962141530')
    if client1.connect():
        if message:
            client1.send_message('+918817401789', message)
            data = {'message':'otp genrated','status':'sucess'}
            return HttpResponse(json.dumps(data),content_type="application/json")
        data = {'message':'otp genrated','status':404}
        return HttpResponse(json.dumps(data),content_type="application/json")
    data = {'message':'otp genrated','status':404}
    return HttpResponse(json.dumps(data),content_type="application/json")
        # client1.send_file('+918817401789', '/home/rails/Downloads/Organization_related_provider.png')

from telethon.tl.types import *
from telethon.tl.functions.contacts import *
from django.http import JsonResponse
def all_list(request):
    data={}
    data_list=[]
    api_id   = 169722
    api_hash = 'b4d4b4374d60a3ba9d7ee84ce010e2b2'
    phone    = '+918962141530'
    client = TelegramClient('+918962141530', api_id, api_hash)
    client.session.try_load_or_create_new(session_user_id='+918962141530')
    if client.connect():
        
        contacts = client.invoke(GetContactsRequest(0))
        users=contacts.users
        for user in users:

            data_list.append ({
                'id':user.id,
                'first_name': user.first_name,
                # 'status':user.status,
                'phone':user.phone,
                })

        data = list(data_list)
        import pdb; pdb.set_trace()
        return HttpResponse(json.dumps(data),content_type="application/json")
        
    data = {'message':'otp genrated','status':404}
    return HttpResponse(json.dumps(data),content_type="application/json")

