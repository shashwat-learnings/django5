from django.shortcuts import render
from django.conf import settings
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from .models import User
from .utils import send_activation_email
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.decorators import login_and_role_required

def send_activation_email_to_user(user:User):
    uid64 = urlsafe_base64_encode(force_bytes(user.pk))
    token=default_token_generator.make_token(user)
    activation_link = reverse(' ',kwargs={'uid64':uid64,'token':token})
    activation_url = f'{settings.SITE_DOMAIN}{activation_link}'
    send_activation_email(user.email,activation_url)

# @login_required
# @login_and_role_required("customer")
def activate_account(request,uid64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)

        if user.is_active:
            messages.warning(request,"This account has already been activated")
            return redirect('login')
        
        if default_token_generator.check_token(user,token):
            user.is_active = True
            user.save()
            messages.success(request,"Your account has been activated successfully")
            return redirect('login')
        else:
            messages.success(request,"Your activation link is invalid or has expired")
            return redirect('login')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist): 
        messages.error(request,"Your activation invalid")
        return redirect('login')

# Create your views here.
