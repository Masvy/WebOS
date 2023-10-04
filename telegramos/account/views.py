from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Profile
import json


def index(request):
    return render(request, 'account/index.html')


def main(request):
    return render(request, 'account/main.html')


def profile(requst):
    return render(requst, 'account/profile.html')


@csrf_exempt
def save_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        name = data.get('name')
        user_name = data.get('user_name')
        # Сохраняем код в базу данных
        profile = Profile(user_id=user_id, name=name,
                          user_name=user_name)
        profile.save()

        return JsonResponse({'message': 'Code saved successfully'}, status=200)

    return JsonResponse({'message': 'Invalid request'}, status=400)


@csrf_exempt
def check_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        user = Profile.objects.filter(user_id=user_id).exists()
        if user:
            return HttpResponse()
        resp = HttpResponse()
        resp.status_code = 404
        return resp


@csrf_exempt
def get_profile(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if not user_id:
            resp = HttpResponse()
            resp.status_code = 400
            return resp
        user: Profile = Profile.objects.get(user_id=user_id)
        if user:
            js = serializers.serialize('json', [ user, ])
            print("\n\n")
            print(js)
            print("\n\n")
            return HttpResponse(js)
        resp = HttpResponse()
        resp.status_code = 404
        return resp

@csrf_exempt
def put_description(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        description = data.get('description')
        if not user_id:
            resp = HttpResponse()
            resp.status_code = 400
            return resp
        user = Profile.objects.get(user_id=user_id)
        if user:
            user.description = description
            user.save()
            return HttpResponse()
        resp = HttpResponse()
        resp.status_code = 404
        return resp
