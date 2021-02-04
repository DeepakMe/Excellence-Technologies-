from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import UserAddress
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import response
import json

# Create your views here.
@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        uname = data['username']
        pwd = data['password']
        user = auth.authenticate(username=uname, password=pwd)
        if user is not None:
            auth.login(request, user)
            login_data = {'login_data':'Welcome '+str(user)+ ' login successful'}
        else:
            login_data = {'login_data':'You have entered the wrong crendentials'}
    return JsonResponse(login_data)

@csrf_exempt
def register(request):
    print('-------------------------> 1) register method', type(request.body))
    if request.method == 'POST': 
        print('----------------------------------> in post', request)
        data = request.body
        data = json.loads(data)
        # print('username : ', request.body['username'], 'password : ', request.body['password'])
        try:
            print('------------------------------------------------------> email : ', data['username'], data['password'])
            User.objects.get(username=str( data['username']))
            register_data = {'data':'Your user is already saved Try nre username'}
        except User.DoesNotExist:
            user = data['username']
            User.objects.create_user(username=user, password=data['password'])
            # return redirect(login)
            register_data = {'data':'Your user is successfully saved'}
    return JsonResponse(register_data)

@csrf_exempt
def add_address(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = data['username']
        street = data['street']
        pincode = data['pincode']
        country = data['country']
        state = data['state']
        contact = data['contact']
        user_address_obj = UserAddress(username=User.objects.get(username=user), 
        user_street=street,
        user_pincode=pincode,
        user_country=country, 
        user_state=state,
        user_contact=contact)
        user_address_obj.save()
    add_address_data = {'data':'Your data is successfully saved'}
    return JsonResponse(add_address_data)

@csrf_exempt
def update_address(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = data['username']
        street = data['street']
        pincode = data['pincode']
        country = data['country']
        state = data['state']
        state = data['state']
        contact = data['contact']
        print('--------------------------------------------------------------->', data)
        try:
            user_address_obj = UserAddress.objects.get(username__username=user, user_contact=contact)
            user_address_obj.user_street = street
            user_address_obj.user_pincode = pincode
            user_address_obj.user_country = country
            user_address_obj.user_state = state
            user_address_obj.save()
            update_address_data = {'data':'Your data is updated successfully'}
            return JsonResponse(update_address_data)
        except Exception as e:
            update_address_data = {'data':'You have entered wrong data of contact or username'}
            print('--------------------------------------------------------------->', vars(user_address_obj))
            return JsonResponse(update_address_data)
        