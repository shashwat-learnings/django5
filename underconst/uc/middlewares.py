from decouple import config
from django.shortcuts import render

from uc.models import UnderConstruction

class UnderConstructionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("UnderConstructionMiddleware initialized")

    def __call__(self, request):
        if request.user.is_staff:
            print("UnderConstructionMiddleware: Staff user, bypassing")
            return self.get_response(request)
        uc_key = config('MAINTENANCE_BYPASS_KEY', default=None)
        if "uc_key" in request.GET and request.GET["uc_key"] == uc_key:
            request.session['bypass_uc'] = True
            request.session.set_expiry(0)  # Session expires on browser close
            print(f"UnderConstructionMiddleware: Bypass key matched, setting session {request.session.get('bypass_uc')}")
        if request.session.get('bypass_uc'):
            print("UnderConstructionMiddleware: Bypass key detected, bypassing")
            return self.get_response(request)
        try:
            uc_status = UnderConstruction.objects.first()
            if uc_status and uc_status.is_under_construction:
                print("UnderConstructionMiddleware before called")
                response = render(request, 'uc/underc.html')
                print("UnderConstructionMiddleware after called")
                return response
        except Exception as e:
            print(f"Error in UnderConstructionMiddleware: {e}")
        print("UnderConstructionMiddleware before called")
        response = self.get_response(request)
        print("UnderConstructionMiddleware after called")
        return response