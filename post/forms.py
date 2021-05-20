from django import forms
from .models import Apply

class CreatePostForm(forms.ModelForm) :
  class Meta:
    model = Apply
    fields = ['image','name', 'age', 'sex', 'body']
