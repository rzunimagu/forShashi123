from django import forms

class UserInputForm(forms.Form):
    user_input = forms.CharField(label='Your code', widget=forms.Textarea())
