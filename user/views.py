from django.http import HttpResponse
from django.template import loader
from .forms import FeestatusForm
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from.models import User
from django.utils import timezone
@csrf_exempt
def members(request):
  template = loader.get_template('createaccount.html')
  return HttpResponse(template.render())
@csrf_exempt
def details(request):
    if request.method == 'POST':
        form = FeestatusForm(request.POST)
        if form.is_valid():
            form.save()
            template=loader.get_template('usersuccess.html')
            return HttpResponse(template.render())
        else:
            # Handle form validation errors here
            return HttpResponse("Form is not valid")
        
@csrf_exempt
def members1(request):
  template = loader.get_template('some.html')
  return HttpResponse(template.render())
@csrf_exempt
def members2(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(user_name=user_name)
            if (password== user.password):
                request.session['user']=user.user_name
                a=user.last_login

                
                # User authenticated, redirect to profile page or return user data
                context={
                   
                    'user':user,
                     'last_login_before_update': a
                    
                
                }
                template=loader.get_template('do.html')
                user.last_login=timezone.now()
                user.save()
                
                
                return HttpResponse(template.render(context, request))
            
            
            else:
                # Invalid credentials, handle accordingly (e.g., show error message)
                pass
        except User.DoesNotExist:
            # Username does not exist, handle accordingly
            pass
    return render(request, 'some.html')
def logout(request):
    del request.session['user']
    return redirect('/login')