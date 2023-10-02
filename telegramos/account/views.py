from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
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
