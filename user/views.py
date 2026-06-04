from http.client import HTTPMessage
from django import template
from django.http import HttpResponse
from django.template import loader
from .forms import UserstatusForm
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from.models import User
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import cache_control, never_cache
from django.utils.decorators import method_decorator
from datetime import datetime
        

@csrf_exempt
#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def auth_view(request):
    if request.user.is_authenticated:
        return redirect('yourdetails')
    
    elif request.method == 'POST':
        return login_view(request)
         
    else:
        return render(request, 'login_page.html')

@never_cache
def show_signup_form(request):
    return render(request, 'createaccount.html')

#@cache_control(no_cache=True, must_revalidate= True, no_store=True)
@csrf_exempt    
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        last_login_before_update = user.last_login
        login(request, user)
        print(last_login_before_update)
        User.objects.filter(user_name=username).update(last_login=timezone.now())
        if last_login_before_update is not None:
            request.session['last_login_before_update'] = last_login_before_update.isoformat()
        response = HttpResponse("Redirecting...") 
        response['HX-Redirect'] = '/yourdetails'  # जहाँ आप यूजर को भेजना चाहते हैं
        return response
    else:
        
        return HttpResponse('<div style="color: red;">Username या Password गलत है!</div>')
        #messages.error(request, "Invalid username or password")
        #return HTTPMessage("Invalid username or password")
        #return render(request, 'login_page.html')
        #return redirect('auth')
    
@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if AuthUser.objects.filter(username=username).first():
            return messages.error(request, "Username already exists")
            # return render(request, 'createaccount.html')
        user = AuthUser.objects.create_user(username=username, password=password, email=email)
        
        login(request, user)
        form = UserstatusForm(request.POST)
       # form.instance.last_login = user.last_login
        if form.is_valid():
            print('*'*50)
            obj = form.save(commit=False)
            obj.last_login = user.last_login
            obj.save()
            user.save()
        return redirect('yourdetails')
    else:
        messages.error(request, "Invalid form submission")
        return render(request, 'createaccount.html')


@login_required(login_url='auth')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@csrf_exempt    
def user_details_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(user_name=request.user.username)
        context = {
            'user': user,
            'last_login_before_update': datetime.fromisoformat(request.session.get('last_login_before_update')) if request.session.get('last_login_before_update') else None
        }
        template = loader.get_template('user_details.html')
        return HttpResponse(template.render(context, request))
    else:
        return redirect('auth')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def logout_view(request):
    logout(request)
    return redirect('auth')