from django import forms

class userinput(forms.Form):
    search = forms.CharField(required=True,max_length=25,label='Input #hashtag')