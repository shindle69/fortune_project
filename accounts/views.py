from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from django.urls import reverse
from accounts.models import MyUser
from datetime import datetime
from django.utils.dateformat import DateFormat
from korean_lunar_calendar import KoreanLunarCalendar
from django.http import HttpResponse
from accounts.forms import RegistrationForm, AccountAuthForm


# Create your views here.

def signup(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.username))
 
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username').lower()
            # email = form.cleaned_data.get('email').lower()
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                raw_password = form.cleaned_data.get('password1')
            else:
                return redirect('accounts:signup')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            # destination = kwargs.get("next")
            destination = get_redirect_if_exists(request)
            if destination: # if destination != None
                return redirect(destination)
            return redirect('today_api:today')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
 
    return render(request, 'accounts/signup.html', context)
 
 
def logout_view(request):
    logout(request)
    return redirect("today_api:today")
 
 
def login_view(request, *args, **kwargs):
    context = {}
 
    user = request.user
    if user.is_authenticated:
        return redirect("today_api:today")
 
    destination = get_redirect_if_exists(request)
    if request.POST:
        form = AccountAuthForm(request.POST)
        if form.is_valid():
            username = request.POST.get('user')
            password = request.POST.get('password')
            user = authenticate(user=username, password=password)
            if user:
                login(request, user)
                if destination:
                    return redirect(destination)
                return redirect("today_api:today")
    else:
        form = AccountAuthForm()
 
    context['login_form'] = form
 
    return render(request, "accounts/login_view.html", context)
 
 
def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


@login_required
def profile(request, pk):
    if request.method == 'POST':
        pass        
    user = get_user_model().objects.get(pk=pk)

    year = user.birth_day.strftime("%Y")
    month = user.birth_day.strftime("%m")
    day = user.birth_day.strftime("%d")
    #
    calendar = KoreanLunarCalendar()
    calendar.setSolarDate(int(year), int(month), int(day))
    lunar = calendar.LunarIsoFormat()
    gabja = calendar.getGapJaString()
    hanja = calendar.getChineseGapJaString()

    # image = user.image.url

    context = {
        "lunar": lunar,
        "gabja": gabja,
        "hanja": hanja,
    }

    return render(request, 'accounts/profile.html', context)

# def signup(request):      

#     if request.method =="POST":        
        
#         username = request.POST["username"]
#         password = request.POST["password"]
#         # first_name = request.POST["first_name"]
#         # last_name = request.POST["last_name"]
#         email = request.POST["email"]
#         nick_name = request.POST["nick_name"]
#         birth_day = request.POST["birth_day"]
#         birth_time = request.POST["birth_time"]    
#         image = request.FILES.get("image")
        
#         user = MyUser.objects.create_user(username, password)
#         # user.first_name = first_name
#         # user.last_name = last_name
#         user.username = username
#         user.password = password 
#         user.name = nick_name
#         user.birth_day = birth_day
#         user.birth_time = birth_time
#         user.email = email
#         user.image = image          
        
#         user.save()
#         return redirect("accounts:login")

#     return render(request, "accounts/signup.html")


# @login_required
# def profile_update(request, pk):
#     if request.method =="POST":
#         print(request.POST)
        
#         username = request.username
#         password = request.POST["password"]
#         first_name = request.POST["first_name"]
#         last_name = request.POST["last_name"]
#         email = request.POST["email"]
#         customer_id = request.POST["customer_id"]
#         birth_day = request.POST["birth_day"]
#         birth_time = request.POST["birth_time"]  
              

#         user = MyUser.objects.create_user(username, password)
#         user.email = email
#         user.first_name = first_name
#         user.last_name = last_name
#         user.customer_id = customer_id
#         user.birth_day = birth_day
#         user.birth_time = birth_time
#         user.save()
#         return redirect("accounts:profile_update")

#     return render(request, "accounts/profile_form.html")



# def login_view(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             print("인증성공")
#             login(request, user)
#             return redirect(reverse("single_pages:landing"))
#         else:
#             print("인증실패")

#     return render(request, "accounts/login_view.html")

# def logout_view(request):
#     logout(request)
#     return redirect('today_api:today')