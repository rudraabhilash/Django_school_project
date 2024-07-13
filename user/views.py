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
            
            # Check if the password matches
            if password == user.password:
                # Set the user in session
                request.session['user'] = user.user_name
                
                # Fetch last login time before updating
                last_login_before_update = user.last_login
                
                # Update last login time to current time
                user.last_login = timezone.now()
                user.save()
                
                # Prepare context to render the template
                context = {
                    'user': user,
                    'last_login_before_update': last_login_before_update
                }
                
                # Render the template with the context
                template = loader.get_template('do.html')
                return HttpResponse(template.render(context, request))
            else:
                # Password is incorrect, show error message
                return render(request, 'some.html', {'error_message': 'Incorrect password.'})
        
        except User.DoesNotExist:
            # Username does not exist, show error message
            return render(request, 'some.html', {'error_message': 'Username does not exist.'})
    
    # Handle GET requests or invalid POST data
    return render(request, 'some.html')
def logout(request):
 if request.session.has_key('user'): 
    del request.session['user']
    return redirect('/login')
 else:
    return redirect('/login')
 
