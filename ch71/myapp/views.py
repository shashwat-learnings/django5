from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import httpx
import time
import asyncio

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Home Page!")


# async def home(request):
#     return HttpResponse("This is an asynchronous view.")


# Synchronous view making an external HTTP request
def sync_view(request):
    start_time = time.time()
    responses =[]
    for _ in range(5):
        response = httpx.get('https://jsonplaceholder.typicode.com/posts')
        responses.append(response)
    # data = response.json()
    data = [resp.json() for resp in responses]
    end_time = time.time()
    print(f"Synchronous view took {end_time - start_time} seconds")
    return JsonResponse({'status': 'success', 'data': data,'time_taken': end_time - start_time})

# Asynchronous view making an external HTTP request
async def async_view(request):
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        tasks = [client.get('https://jsonplaceholder.typicode.com/posts') for _ in range(5)]
        responses = await asyncio.gather(*tasks)
    data = [resp.json() for resp in responses]
    end_time = time.time()
    # data['elapsed_time'] = end_time - start_time 
    print(f"Asynchronous view took {end_time - start_time} seconds")
    return JsonResponse({'status': 'success', 'data': data, 'time_taken': end_time - start_time}) 