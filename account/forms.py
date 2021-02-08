from django import forms
from account.models import User

class UserLoginForm(forms.ModelForm):
     
    #loading_time= forms.TimeField(widget=widgets.AdminTimeWidget)
    userid = forms.CharField(required=True, label='Username*',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=True, label='Password*',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    
    class Meta:
        model = User
        fields = [ 'userid', 'password']
        #  fields=['site','name',]
        exclude = ['firstname','lastname','mobileno','worklocation','status','version','created','createdby','updated','updatedby']

