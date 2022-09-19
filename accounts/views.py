from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import MyUser
from datetime import datetime
from django.utils.dateformat import DateFormat
from korean_lunar_calendar import KoreanLunarCalendar


# Create your views here.
def signup(request):
    if request.method =="POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        customer_id = request.POST["customer_id"]
        birth_day = request.POST["birth_day"]
        birth_time = request.POST["birth_time"]

        user = MyUser.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.customer_id = customer_id
        user.birth_day = birth_day
        user.birth_time = birth_time
        user.save()
        return redirect("accounts:login")

    return render(request, "accounts/signup.html")

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

    context = {
        "lunar": lunar,
        "gabja": gabja,
        "hanja": hanja,
    }

    return render(request, 'accounts/profile.html', context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
        else:
            print("인증실패")
    return render(request, "accounts/login_view.html")

def logout_view(request):
    logout(request)
    return redirect('accounts:login')