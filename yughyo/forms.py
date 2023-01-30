from django import forms
from .models import Question

from django.forms import Textarea

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['category', 'question_text', ]
        widgets = {
            'question_text': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 1200px;',
                'placeholder': '궁금한 것을 입력하세요.'
            })
        }

