from django.shortcuts import render
from django.http import JsonResponse

def multiply(request,n):
#   if request.method == 'GET':
#     number = request.GET.get('number')
#     print(number)
    # if number:
    #   result = int(number) * 10
    #   return JsonResponse({'result': result})
    if(n):
        return JsonResponse({'result': n})
    else:
      return JsonResponse({'error': 'Missing number parameter'}, status=400)
#   else:
#     return JsonResponse({'error': 'Unsupported method'}, status=405)
