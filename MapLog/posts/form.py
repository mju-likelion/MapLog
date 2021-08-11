from django import forms
from .models import Posts

class DetailForm(forms.ModelForm):
    #수정시 기존 글을 불러오기 위한 Form
    class Meta:
        model = Posts
        fields = ['title', 'pick_date', 'music', 'description', 'image']