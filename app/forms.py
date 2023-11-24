from django import forms
from .models import Todo



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "description")

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter Todo'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].label = ''
        
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['row'] = '30'
        self.fields['description'].widget.attrs['col'] = '5'
        self.fields['description'].label = ''