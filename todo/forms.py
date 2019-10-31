from .models import Todo
from django.forms import ModelForm, TextInput


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        #fields = ['content', 'added_time']
        fields = '__all__'

        labels = {

            'content': 'Nice Content',
            'title': 'This is nice Title'
        }
        widgets = {
            'content': TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp', 'placeholder': 'Enter Content'}),
            'title': TextInput(attrs={'class': 'form-control', 'id': 'titleHere', 'aria-describedby': 'titleHelp', 'placeholder': 'Enter Title Here...'})
        }
