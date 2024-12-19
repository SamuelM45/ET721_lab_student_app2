from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45,
                           widget=forms.TextInput(attrs={'id':'task','class' : 'todo_text', 'placeholder' :'type your task...', 'aria-label' :'Todo', 'aria-describeby' : 'add-btn'}))