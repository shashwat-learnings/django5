from django.shortcuts import render
from django.http import Http404
from datetime import datetime, timedelta, timezone

# Create your views here.
def setsession(request):
    # raise Http404("Ignore this view")
    request.session['fname'] = 'Django Session'
    request.session['lname'] = 'Django Session'
    # request.session.set_expiry(300)  # Session will expire in 5 minutes
    # request.session.set_expiry(0)  # Session will expire when the browser is closed
    return render(request, 'student/setsession.html')

def getsession(request):
    fname = request.session.get('fname', 'Guest')
    lname = request.session.get('lname', 'Guest')
    return render(request, 'student/getsession.html', {'fname': fname + ' ' + lname, })


def deletesession(request):
    try:
        del request.session['fname']
    except KeyError:
        pass
    try:
        del request.session['lname']
    except KeyError:
        pass
    return render(request, 'student/delsession.html')

def flushsession(request):
    request.session.flush() # Deletes the session data and the session cookie which are not expired
    return render(request, 'student/flushsession.html')

def sessionmethodsinview(request):
    keys = request.session.keys()
    values = request.session.values()
    items = request.session.items()

    age = request.session.setdefault('age', 31) # Set default age if not present
    
    session_cookie_age = request.session.get_session_cookie_age()  # in seconds
    expire_age = request.session.get_expiry_age()  # in seconds
    expiry_datetime = request.session.get_expiry_date()  # datetime object
    expire_at_browser_close = request.session.get_expire_at_browser_close()  # boolean
    context = {
        'keys': keys,   
        'values': values,
        'items': items,
        'age': age,
        'session_cookie_age': session_cookie_age,
        'expire_age': expire_age,
        'expiry_datetime': expiry_datetime,
        'expire_at_browser_close': expire_at_browser_close,
    }
    # # Set session     expiry to 1 minute from now
    # request.session.set_expiry(60)  # 60 seconds
    return render(request, 'student/sessionmethodsinview.html',context=context)

def sessionmethodsintemplate(request):
    # # Set session expiry to 1 minute from now
    # request.session.set_expiry(60)  # 60 seconds
    return render(request, 'student/sessionmethodsintemplate.html')

def sessionclear(request):
    # # Manually clear expired sessions 
    request.session.clear_expired() # clear expired sessions else flush can be used to clear all sessions
    return render(request, 'student/sessionclear.html')

def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'student/settestcookie.html')

def checktestcookie(request):
    if request.session.test_cookie_worked():
        message = "Test cookie worked!"
        request.session.delete_test_cookie()
    else:
        message = "Test cookie did not work."
    return render(request, 'student/checktestcookie.html')

def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'student/deltestcookie.html')