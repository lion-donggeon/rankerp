from django import forms
from django.forms import widgets
from main.models import Question, Answer, Comment
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

class QuestionForm(forms.ModelForm):

    content = SummernoteWidget()

    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content', 'image']  # QuestionForm에서 사용할 Question 모델의 속성
       
        widgets = {
            'content': SummernoteWidget(),
        }
        
        labels = {
            'subject': '제목',
            'content': '내용',
        }  

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }