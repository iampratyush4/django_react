# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from polygon import RESTClient
# import requests



# def multiply(request,n):

#     if(int(n)>0):
#         print("i am here")
#         response = requests.get("https://api.polygon.io/v2/aggs/ticker/AAPL/prev?adjusted=true&apiKey=4FPAmNwQcdi9ErtGYTMFQop0gsvOSTY2")
#         return HttpResponse(response.json())
#     else:
#       return JsonResponse({'error': 'Missing number parameter'}, status=400)
from django.http import JsonResponse
from django.views import View
import requests


def multiply(request, n):
    try:
        n = int(n)
        result = n * 10
        response = requests.get("https://api.polygon.io/v2/aggs/ticker/AAPL/prev?adjusted=true&apiKey=4FPAmNwQcdi9ErtGYTMFQop0gsvOSTY2")
        # return JsonResponse({'result': result})
        main_data=response.json()
        print(main_data['results'][0]['c'])
        return JsonResponse({'result': main_data})
    except ValueError:
        return JsonResponse({'error': 'Invalid input. Please provide a valid integer.'}, status=400)


