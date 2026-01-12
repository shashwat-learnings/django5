from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['fname'] = 'John'
    return render(request, 'student/setsession.html')

def getsession(request):
    fname = request.session.get('fname', 'Guest')
    return render(request, 'student/getsession.html', {'fname': fname})

def sessionclear(request):

   request.session.flush()
   request.session.clear_expired()
   return render(request, 'student/sessionclear.html')