from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import Member,Emi,Loan, Group
from .forms import MemberForm,EmiForm,Emiform,Loanform,Signupform, Loginform
from django.utils.cache import patch_cache_control
from django.shortcuts import get_object_or_404
from django.db.models  import Sum,Count
from datetime import date
from Kuzhu_project import settings
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def home(request):
    if request.user.is_authenticated:
        try:
            template_tag = True
            member_count = Member.objects.count()
            loanamount = Member.objects.aggregate(Sum("Loanamount"))
            intrest = Emi.objects.aggregate(Sum("Intrest"))
            member = Member.objects.get(pk=1)
            total_emi = Emi.objects.filter(mem_id=member.id).count()
            return render(request, "kuzhuapp/home.html", context={"tt":template_tag,"member":member_count,"loanamount":loanamount,"total_emi":total_emi,"intrest":intrest})
        except:
            return render(request, "kuzhuapp/home.html")
    else:
        return redirect("login")


def signup(request):
    form = Signupform()
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "User created Successfully")
            return redirect("/login/")
        else:
            form = Signupform(request.POST)
            response = render(request, "kuzhuapp/signup.html" , context={"form":form})
            patch_cache_control(response, no_store=True)
            return response


    response = render(request, "kuzhuapp/signup.html" , context={"form":form})
    patch_cache_control(response, no_store=True)
    return response



@login_required(login_url="/login/")
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.INFO, "Logged out Successfully")
        return redirect("/login/")



@login_required(login_url="/login/")
def listmember(request):
    if request.user.is_authenticated:
        member = Member.objects.all()
        return render(request, 'kuzhuapp/member.html', context={"member":member})
    else:
        return redirect("login")


@login_required(login_url="/login/")
def Addmember(request):
    if request.user.is_authenticated:
        form = MemberForm()
        if request.method == "POST":
            form = MemberForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Member Created Successfully')
                return redirect("home")
            else:
                response = render(request,'kuzhuapp/addmember.html',context={"form":form})
                patch_cache_control(response, no_store=True)
                return response
        response = render(request,'kuzhuapp/addmember.html',context={"form":form})
        patch_cache_control(response, no_store=True)
        return response
    else:
        return redirect("login")


@login_required(login_url="/login/")
def Addemi(request, id):
    if request.user.is_authenticated:
        member = Member.objects.get(id=id)
        form = Emiform()
        if request.method == "POST":
            form = Emiform(request.POST)
            if form.is_valid():
                amount = form.cleaned_data['repay']
                intrest = form.cleaned_data['Intrest']
                savings = form.cleaned_data['Savings']
                sandha = form.cleaned_data['Sandha']
                total = amount+intrest+savings+sandha
                group = Group(repay=amount, intrest=intrest,savings=savings, sandha=sandha, total=total)
                group.save()
                member.Loanamount = int(member.Loanamount)-amount
                member.save()
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Emi Added Successfully')
                return redirect("/members/")
            else:
                context = {"form":form, "id":id}
                return render(request, "kuzhuapp/addemi.html",context)
        response = render(request,'kuzhuapp/addemi.html',context={"form":form,"member":member,"id":id})
        patch_cache_control(response, no_store=True)
        return response
    else:
        return redirect("login")



@login_required(login_url="/login/")
def Updatemember(request,id):
    if request.user.is_authenticated:
        member = Member.objects.get(id=id)
        form = MemberForm(instance=member)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Member Created Successfully')
                return redirect("home")
            else:
                form =  MemberForm(request.POST, request.FILES)
                response = render(request,'kuzhuapp/updatemember.html',context={"form":form, "id":id})
                patch_cache_control(response, no_store=True)
                return response

        response = render(request,'kuzhuapp/updatemember.html',context={"form":form, "id":id})
        patch_cache_control(response, no_store=True)
        return response
    else:
        return redirect("login")


@login_required(login_url="/login/")
def Memberlist(request):
    if request.user.is_authenticated:
        member = Member.objects.all()
        return render(request, "kuzhuapp/Memberlist.html", context={"member":member})
    else:
        return redirect("login")


@login_required(login_url="/login/")
def Memberdashboard(request,id):
    if request.user.is_authenticated:
        member = Member.objects.get(id=id)
        emi = Emi.objects.filter(mem_id=member.id)
        return render(request, "kuzhuapp/memberdashboard.html", context={"member":member,"emi":emi})
    else:
        return redirect("login")


@login_required(login_url="/login/")
def loandispurse(request):
    if request.user.is_authenticated:
        try:
            group = Group.objects.filter(mon=date.today()).first()
            total = group.total
        except:
            total = 0
        form = Loanform()
        if request.method == "POST":
            form = Loanform(request.POST)
            if form.is_valid():
                mem = form.cleaned_data['mem']
                loan = form.cleaned_data['loan']
                member = Member.objects.get(pk=mem.id)
                member.Loanamount += loan
                if total > 0:
                    group.total = total -loan
                    group.save()
                member.save()
                form.save()
                return redirect('/loandispurse/')
            else:
                form = Loanform(request.POST)
                response = render(request,'kuzhuapp/loandispursement.html',context={"form":form, "amount":total})
                patch_cache_control(response, no_store=True)
                return response
        else:
            response = render(request,'kuzhuapp/loandispursement.html',context={"form":form, "amount":total})
            patch_cache_control(response, no_store=True)
            return response
    else:
        return redirect("login")


@login_required(login_url="/login/")
def delete_member(request, id):
    if request.user.is_authenticated:
        member = get_object_or_404(Member, id=id)
        member.delete()
        messages.add_message(request, messages.SUCCESS, "Member Record deleted !")
        return redirect("/members/")
    else:
        return redirect("login")
