from django.contrib import admin
from .models import Member,Emi
# Register your models here.


class Memberadmin(admin.ModelAdmin):
    fields=['Name','Age','Gaurdian','Aadhaarnumber','Pannumber','Loanamount','Image']


class Emiadmin(admin.ModelAdmin):
    fields=['mem','repay','Intrest','Savings','Sandha']


admin.site.register(Member, Memberadmin)
admin.site.register(Emi, Emiadmin)