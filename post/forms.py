from django import forms
from .models import Post

class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'time', 'type_meet', 'place', 'content', 'min_count', 'max_count'}
        widgets = {'time' : DateInput()}