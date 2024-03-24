from pyexpat import model
from django import forms
from .models import Member,Emi,Loan
from django.contrib.auth.models import User


class Signupform(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class Loginform(forms.Form):
    Username = forms.CharField(max_length=25,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
    Password = forms.CharField(max_length=25,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))

    
class Loanform(forms.ModelForm):
    class Meta:
        model = Loan
        exclude = ("mon",)



class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ("emis",)




class Emiform(forms.ModelForm):
    class Meta:
        model = Emi
        fields = "__all__"


class EmiForm(forms.Form):
    member = forms.CharField(max_length=25,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Name","id":"memberNameInput"}))
    Repay = forms.DecimalField(max_digits=10, decimal_places=2,widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Repay"}))
    Intrest = forms.DecimalField(max_digits=10, decimal_places=2,widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Intrest"}))
    Savings = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Savings"}))
    Sandha = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Sandha"}))
