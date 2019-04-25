
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from .forms import *
from .models import Users


def index(request):
    return render(request, 'myapp/home.html')


def home(request):
    return render(request, 'myapp/home.html')


def credit(request):
    form = amount()
    return render(request, 'myapp/credit.html',{ 'form':form, })

def mkcredit(request):
    form = amount(request.POST)
    if form.is_valid():
        amt = form.cleaned_data['Amount']
        name = request.session['user']
        print(amt)
        print(type(amt))


        try :
            user = Users.objects.get(Username=name)


            if amt > 0 :
                user.Balance+=amt
                print(type(user.Balance))
                user.save()
                #Users.objects.filter(Username=name).update(Balance=user.Balance)
                msg="Success"
                return render(request,'myapp/loginsuccess.html',{'msg':msg,'balance':user.Balance})
            else :
                form = amount()
                error = "amount not vaild"
                return render(request,'myapp/credit.html',{'form':form,'error':error})

        except Exception as e :
            form = signup()
            return render(request,'myapp/signup.html',{'form':form,'error':"No such user Exist \n Please Signup"})


def Login(request) :
    form = login()
    return render(request, 'myapp/login.html',{ 'form':form, })

def Signup(request):
    form = signup()
    return render(request, 'myapp/signup.html',{ 'form':form, })


def contact(request):
    return render(request, 'myapp/contact.html')

def loginsuccess(request):
    form = login(request.POST)
    if form.is_valid():
        name = form.cleaned_data['Username']
        password = form.cleaned_data['Password']
        try :
            user = Users.objects.get(Username=name)
            if password == user.Password :
                request.session['user'] = name
                request.session['password'] = password
                return render(request,'myapp/loginsuccess.html',{'name':name,'password':password})
            else :
                form = login()
                error = "Invalid Password Try Again"
                return render(request,'myapp/home.html',{'form':form,'error':error})

        except Exception as e :
            form = signup()
            return render(request,'myapp/signup.html',{'form':form,'error':"No such user Exist \n Please Signup"})


    else :
        return HttpResponse("<h1>Form is not valid</h1>")

def mksignup(request):
    form = signup(request.POST)
    if form.is_valid():
        Confirm_password = form.cleaned_data['Confirm_Password']
        Password = form.cleaned_data['Password']
        if Password == Confirm_password:
            data = {
            'Username' : form.cleaned_data['Username'],
            'Password' : Password,
            'First_Name' : form.cleaned_data['First_Name'],
            'Last_Name' : form.cleaned_data['Last_Name'],
            'Email'  : form.cleaned_data['Email'],
            'Address'   :form.cleaned_data['Address'],

            }
            obj = Users.objects.create(**data)
            obj.save()
            return render(request,'myapp/signupdone.html',{ 'data':data })

        else:
            return render(request,'myapp/signup.html',{'error':'Password not same'})


    else :
        return HttpResponse("<h1>Form is not valid</h1>")


def debit(request):
    form = amount()
    return render(request, 'myapp/debit.html',{ 'form':form, })

def chk(request):
    name = request.session['user']
    user=Users.objects.get(Username=name)
    return render(request,'myapp/chkbal.html',{'Balance':user.Balance})


def mkdebit(request):
    form = amount(request.POST)
    if form.is_valid():
        amt = form.cleaned_data['Amount']
        name = request.session['user']
        print(amt)
        #print(type(amt))


        try :
            user = Users.objects.get(Username=name)


            if amt <= user.Balance and amt>0 :
                user.Balance-=amt
                print(type(user.Balance))
                user.save()
                #Users.objects.filter(Username=name).update(Balance=user.Balance)
                msg="Success"
                return render(request,'myapp/loginsuccess.html',{'msg':msg,'balance':user.Balance})
            else :
                form = amount()
                error = "amount not available"
                return render(request,'myapp/debit.html',{'form':form,'error':error})

        except Exception as e :
            form = signup()
            return render(request,'myapp/signup.html',{'form':form,'error':"No such user Exist \n Please Signup"})

def about(request):
     return render(request,'myapp/about.html')