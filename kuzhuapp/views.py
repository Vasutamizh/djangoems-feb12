from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import Member,Emi,Loan
from .forms import MemberForm,EmiForm,Emiform,Loanform,Signupform, Loginform
from django.utils.cache import patch_cache_control
from django.shortcuts import get_object_or_404
from django.db.models  import Avg,Sum,Count
from datetime import date


def home(request):
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

def loginview(request):
    form = Loginform()
    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            user =  authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('/login')
        else:
            messages.add_message(request, messages.INFO, "Invalid Credentials !")
            response = render(request, "kuzhuapp/login.html", context={"form":form})
            patch_cache_control(response, no_store=True)
            return response
        
    response = render(request, "kuzhuapp/login.html", context={"form":form})
    patch_cache_control(response, no_store=True)
    return response
        


def listmember(request):
    member = Member.objects.all()
    return render(request, 'kuzhuapp/member.html', context={"member":member})


def Addmember(request):
    form = MemberForm()
    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Member Created Successfully')
            return redirect("home")
        else:
            response = render(request,'kuzhuapp/Addmember.html',context={"form":form})
            patch_cache_control(response, no_store=True)
            return response
    response = render(request,'kuzhuapp/Addmember.html',context={"form":form})
    patch_cache_control(response, no_store=True)
    return response


def Addemi(request, id):
    member = Member.objects.get(id=id)
    form = Emiform()
    if request.method == "POST":
        form = Emiform(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['repay']
            member.Loanamount = int(member.Loanamount)-amount
            member.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Emi Added Successfully')
            return redirect("/members/")
        else:
            context = {"form":form}
            return render(request, "kuzhuapp/addemi.html",context)
    response = render(request,'kuzhuapp/addemi.html',context={"form":form,"member":member})
    patch_cache_control(response, no_store=True)
    return response



def Updatemember(request,id):
    member = Member.objects.get(id=id)
    form = MemberForm(instance=member)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Member Created Successfully')
            return redirect("home")
        else:
            form =  MemberForm(request.POST, request.FILES)
            response = render(request,'kuzhuapp/updatemember.html',context={"form":form})
            patch_cache_control(response, no_store=True)
            return response

    response = render(request,'kuzhuapp/updatemember.html',context={"form":form})
    patch_cache_control(response, no_store=True)
    return response


def Memberlist(request):
    member = Member.objects.all()
    return render(request, "kuzhuapp/Memberlist.html", context={"member":member})



def Memberdashboard(request,id):
    member = Member.objects.get(id=id)
    emi = Emi.objects.filter(mem_id=member.id)
    return render(request, "kuzhuapp/memberdashboard.html", context={"member":member,"emi":emi})


def loandispurse(request):
    total_amount = Emi.objects.filter(mon=date.today()).aggregate(repay=Sum("repay"),intrest=Sum("Intrest"),savings=Sum("Savings"),sandha=Sum("Sandha"))
    try:
        if total_amount:
            amount = total_amount['repay']+total_amount['intrest']+total_amount['intrest']+total_amount['savings']+total_amount['sandha']
    except:
        amount = 0
    form = Loanform()
    if request.method == "POST":
        form = Loanform(request.POST)
        if form.is_valid():
            mem = form.cleaned_data['member']
            loan = form.cleaned_data['loan']
            member = Member.objects.get(pk=mem.id)
            member.Loanamount += loan
            amount -= loan
            member.save()
            form.save()
            return redirect('/loandispurse/')
        else:
            response = render(request,'kuzhuapp/loandispursement.html',context={"form":form, "amount":amount})
            patch_cache_control(response, no_store=True)
            return response

    else:
        response = render(request,'kuzhuapp/loandispursement.html',context={"form":form, "amount":amount})
        patch_cache_control(response, no_store=True)
        return response


def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    messages.add_message(request, messages.SUCCESS, "Member Record deleted !")
    return redirect("/members/")
