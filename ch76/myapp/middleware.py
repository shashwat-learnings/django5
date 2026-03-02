from asgiref.sync import iscoroutinefunction, markcoroutinefunction
from django.utils.decorators import sync_and_async_middleware, sync_only_middleware, async_only_middleware


@sync_and_async_middleware
# @sync_only_middleware , will only work with synchronous views, if you try to use it with asynchronous views, it will raise an error.
# @async_only_middleware, will only work with asynchronous views, if you try to use it with synchronous views, it will raise an error.
def my_middleware(get_response):
    print("One time configuration and initialization.")
    if iscoroutinefunction(get_response):
        print("This is an asynchronous middleware.")
    else:
        print("This is a synchronous middleware.")

    def middleware(request):
        print("Before view")
        response = get_response(request)
        print("After view")
        return response

    return middleware

class MyMiddleware:
    async_capable = True
    sync_capable = False
    def __init__(self, get_response):
        self.get_response = get_response
        if iscoroutinefunction(get_response):
            markcoroutinefunction(self)
        print("One time configuration and initialization.")

    def __call__(self, request):
        print("Before view")
        response = self.get_response(request)
        print("After view")
        return response 