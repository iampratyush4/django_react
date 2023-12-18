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
import random
from django.http import JsonResponse
from django.views import View
import requests


def multiply(request, n):
    try:
        n = int(n)
        result = n * 10
        response = requests.get("https://api.polygon.io/v2/aggs/ticker/AAPL/prev?adjusted=true&apiKey=4FPAmNwQcdi9ErtGYTMFQop0gsvOSTY2")
        # return JsonResponse({'result': result})
        # main_data=response.json()
        # print(main_data['results'][0]['c'])
        # all_data=requests.get("https://api.polygon.io/v3/reference/tickers?active=true&apiKey=4FPAmNwQcdi9ErtGYTMFQop0gsvOSTY2")
        # print(all_data)
        # if 'results' in all_data:
            
        #     all_symbols = [ ticker['symbol'] for ticker in  all_data['results']]
        #     random_symbols = random.sample(all_symbols, 3)
        #     print(random_symbols,"here")
            
            # Your Polygon.io API key
        api_key = "4FPAmNwQcdi9ErtGYTMFQop0gsvOSTY2"

        # Number of tickers you want to select
        

        # Get active tickers
        active_tickers = get_active_tickers(api_key)
  
        # Select a random subset of tickers
        if active_tickers:
            selected_tickers = random.sample(active_tickers, min(n, len(active_tickers)))

            # Create a list of dictionaries with ticker and stock price
            stock_list = []
            for ticker in selected_tickers:
                price = get_stock_price(ticker, api_key)
                if price is not None:
                    stock_list.append({ticker: price})

            print(stock_list)
        else:
            print("Failed to retrieve tickers.")
        return JsonResponse({'result': stock_list})
    except ValueError:
        return JsonResponse({'error': 'Invalid input. Please provide a valid integer.'}, status=400)
    
def get_active_tickers(api_key):
    api_endpoint = "https://api.polygon.io/v3/reference/tickers"
    params = {'active': 'true', 'apiKey': api_key}
    response = requests.get(api_endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        tickers = [ticker['ticker'] for ticker in data['results']]
        return tickers
    else:
        return []

# Function to get stock price for a given ticker using Polygon.io API
def get_stock_price(ticker, api_key):
    api_endpoint = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/prev"
    params = {'apiKey': api_key}
    response = requests.get(api_endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        # Extracting closing price
        close_price = data['results'][0]['c']
        return close_price
    else:
        return None

# def main():
#     # Your Polygon.io API key
#     api_key = "4FPAmNwQcdi9ErtGYTMFQop0gsvOSTY2"

#     # Number of tickers you want to select
#     n = 5

#     # Get active tickers
#     active_tickers = get_active_tickers(api_key)

#     # Select a random subset of tickers
#     if active_tickers:
#         selected_tickers = random.sample(active_tickers, min(n, len(active_tickers)))

#         # Create a list of dictionaries with ticker and stock price
#         stock_list = []
#         for ticker in selected_tickers:
#             price = get_stock_price(ticker, api_key)
#             if price is not None:
#                 stock_list.append({ticker: price})

#         print(stock_list)
#     else:
#         print("Failed to retrieve tickers.")


