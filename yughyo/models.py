from django.db import models
from accounts.models import MyUser
from django.conf import settings

# Create your models here.
class Iching(models.Model):
    g_id = models.IntegerField(primary_key=True)
    g_name = models.CharField(max_length=30)
    g_content = models.CharField(max_length=500)
    h_content_1 = models.CharField(max_length=500)
    h_content_2 = models.CharField(max_length=500)
    h_content_3 = models.CharField(max_length=500)
    h_content_4 = models.CharField(max_length=500)
    h_content_5 = models.CharField(max_length=500)
    h_content_6 = models.CharField(max_length=500)
    hope = models.CharField(max_length=500)
    consult = models.CharField(max_length=500)
    business = models.CharField(max_length=500)
    trade = models.CharField(max_length=500)
    contract = models.CharField(max_length=500)
    law = models.CharField(max_length=500)
    job = models.CharField(max_length=500)
    promotion = models.CharField(max_length=500)
    school = models.CharField(max_length=500)
    move = models.CharField(max_length=500)
    travel = models.CharField(max_length=500)
    love = models.CharField(max_length=500)
    marry = models.CharField(max_length=500)

    class Meta:
        ordering = ['g_name']


class Question(models.Model):
    CATEGORY_CHOICES = (
        ('hope', '소원'), ('consult', '상담'), ('business', '사업'), ('trade', '매매'),
        ('contract', '계약'), ('law', '소송'), ('job', '취업'), ('promotion', '승진/진급'),
        ('school', '입학'), ('move', '이사'), ('travel', '여행'), ('love', '연애/사랑'), ('marry', '결혼')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    question_text = models.CharField(max_length=200)
    jum = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

#
# class Choice(models.Model):
#     question = models.OneToOneField(Question, on_delete=models.CASCADE)
#     result_number = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
# class Result(models.Model):
#     result_name = models.OneToOneField(Iching, on_delete=models.CASCADE)