from django.shortcuts import render
from today_api.models import Today12

from datetime import datetime
from django.utils.dateformat import DateFormat

from korean_lunar_calendar import KoreanLunarCalendar

# Create your views here.
def mytoday(request):
    today = DateFormat(datetime.now()).format('Ymd') #연월일 20220909
    today_year = DateFormat(datetime.now()).format('Y') #연
    today_month = DateFormat(datetime.now()).format('m') #월
    today_day = DateFormat(datetime.now()).format('d') #일
    key = int(int(today) % 365)   #20220909 / 365 나머지
    dataset = Today12.objects.get(id=key)

    calendar = KoreanLunarCalendar()
    calendar.setSolarDate(int(today_year), int(today_month), int(today_day))
    lunar = calendar.LunarIsoFormat()
    gabja = calendar.getGapJaString()
    hanja = calendar.getChineseGapJaString()

    context = {
        "today": today,
        "key": key,
        "today_year": today_year,
        "today_month": today_month,
        "today_day": today_day,
        "dataset": dataset,
        "lunar": lunar,
        "gabja": gabja,
        "hanja": hanja,
    }
    return render(request, "my_today/mytoday.html", context)
