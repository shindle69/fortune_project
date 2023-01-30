from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import MyUser

# Create your views here.

@login_required
def about(request, pk):
    if request.method == 'POST':
        pass
    # user = get_user_model().objects.get(pk=pk)

    # year = user.birth_day.strftime("%Y")
    # month = user.birth_day.strftime("%m")
    # day = user.birth_day.strftime("%d")
    # #
    # calendar = KoreanLunarCalendar()
    # calendar.setSolarDate(int(year), int(month), int(day))
    # lunar = calendar.LunarIsoFormat()
    # gabja = calendar.getGapJaString()
    # hanja = calendar.getChineseGapJaString()

    # context = {
    #     "lunar": lunar,
    #     "gabja": gabja,
    #     "hanja": hanja,
    # }

    return render(request, 'accounts/profile.html',)
