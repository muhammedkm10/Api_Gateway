import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import json
# Create your views here.




@csrf_exempt
def auth_service(request,action):
    auth_service_url = os.getenv("AUTH_SERVICE_URL")
    service_url = f'{auth_service_url}{action}'
    headers = {
        "Authorization": request.headers.get("Authorization", ""),
        "Content-Type": "application/json",
    }
    try:
        if request.method == "POST":
            body = json.loads(request.body.decode("utf-8"))
            response = requests.post(service_url, json=body, headers=headers)
            return JsonResponse(response.json(),status = response.status_code)
    except Exception as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse({"message":"this is the response"})
