
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import MyUser
from .forms import QuestionForm
from .models import Iching, Question
from accounts.models import MyUser

from django.utils import timezone
import random

# Create your views here.
def iching(request,pk):
    data_list = Iching.objects.get(g_id=pk)
    g_id = data_list.g_id
    g_name = data_list.g_name
    g_content = data_list.g_content
    h_content_1 = data_list.h_content_1
    h_content_2 = data_list.h_content_2
    h_content_3 = data_list.h_content_3
    h_content_4 = data_list.h_content_4
    h_content_5 = data_list.h_content_5
    h_content_6 = data_list.h_content_6
    hope = data_list.hope
    consult = data_list.consult
    business = data_list.business
    trade = data_list.trade
    contract = data_list.contract
    law = data_list.job
    job = data_list.job
    promotion = data_list.promotion
    school = data_list.school
    move = data_list.move
    travel = data_list.travel
    love = data_list.love
    marry = data_list.marry

    context = {
        'g_id': g_id,
        'g_name': g_name,
        'g_content': g_content,
        'h_content_1': h_content_1,
        'h_content_2': h_content_2,
        'h_content_3': h_content_3,
        'h_content_4': h_content_4,
        'h_content_5': h_content_5,
        'h_content_6': h_content_6,
        'hope': hope,
        'consult': consult,
        'business': business,
        'trade': trade,
        'contract': contract,
        'law': law,
        'job': job,
        'promotion': promotion,
        'school': school,
        'move': move,
        'travel': travel,
        'love': love,
        'marry': marry
    }

    return render(request, "yughyo/list.html", context)


@login_required(login_url="../accounts/login")
def front(request):
    list = Question.objects.filter(user=request.user)
    context = {
        'list': list,
    }
    return render(request, 'yughyo/front.html', context)

@login_required
def question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_at = timezone.now()
            question.jum = random.randint(1, 64)
            question.user = request.user
            question.save()
            return redirect('yughyo:detail', pk=question.id)
    else:
        form = QuestionForm()
        context = {'form': form}
    return render(request, 'yughyo/input.html', context)


@login_required
def detail(request, pk):
    question = Question.objects.get(pk=pk)
    cat = question.category
    jum_id = question.jum
    question_text = question.question_text
    iching = Iching.objects.get(pk=jum_id)
    user = question.user

    if cat == "hope":
        jum = iching.hope
    elif cat == "consult":
        jum = iching.consult
    elif cat == "business":
        jum = iching.business
    elif cat == "trade":
        jum = iching.trade
    elif cat == "contract":
        jum = iching.contract
    elif cat == "law":
        jum = iching.law
    elif cat == "job":
        jum = iching.job
    elif cat == "promotion":
        jum = iching.promotion
    elif cat == "school":
        jum = iching.school
    elif cat == "move":
        jum = iching.move
    elif cat == "travel":
        jum = iching.travel
    elif cat == "love":
        jum = iching.love
    elif cat == 'marry':
        jum = iching.marry
    else:
        print(f"더 이상 데이터가 없습니다.")

    g_name = iching.g_name
    g_content = iching.g_content

    myBirthDay = user.birth_day
    myBirthTime = user.birth_time
    createdTime = question.created_at

    context = {
        'question': question_text,
        'category': cat,
        'jum': jum,
        'name': g_name,
        'content': g_content,
        'user': user,
        'birth_day': myBirthDay,
        'birth_time':myBirthTime,
        'createdTime': createdTime
    }
    if request.user != question.user:
        return redirect("{% url 'today_api:today' %}")
    else:
        return render(request, 'yughyo/detail.html', context)

def result(request, pk):
    result = Iching.objects.get(pk=pk)

