from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from today_api.models import Today12
from today_api.serializers import Today12Serializer

from datetime import datetime
from django.utils.dateformat import DateFormat

from korean_lunar_calendar import KoreanLunarCalendar


@api_view()
def today12(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        today_12 = Today12.objects.get(pk=pk)
    except Today12.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Today12Serializer(today_12)
        return Response(serializer.data)

def today_catch(request):
    today = DateFormat(datetime.now()).format('Ymd')
    today_year = DateFormat(datetime.now()).format('Y')
    today_month = DateFormat(datetime.now()).format('m')
    today_day = DateFormat(datetime.now()).format('d')
    key = int(int(today) % 365)
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
    return render(request, "today_api/today.html", context)
