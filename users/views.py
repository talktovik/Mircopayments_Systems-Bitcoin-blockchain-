from django.shortcuts import render, get_object_or_404 , redirect
from main.models import Main
from .models import UsersData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from mytransactions.models import Transactiondata
# Create your views here.

def my_register(request):
    title = Main.objects.get(pk=1)
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(uname,email,password1,password2)

        if password1 != password2:
            error = "PASSWORD DIDN'T MATCHED"
            return render(request,"blog/error.html", {'error':error})

        if len(password1) < 8:
            error = "PASSWORD VERY SMALL"
            return render(request,"blog/error.html", {'error':error})
        if len(User.objects.filter(username= uname)) == 0 and len(User.objects.filter(email=email)) == 0:

            user = User.objects.create_user(username=uname,email= email,password=password1)
            b = UsersData(username = uname,email= email )
            b.save()


    return render(request,'users/home.html',{"title":title})

def mylogin(request):
    title = Main.objects.get(pk=1)
    if request.method == 'POST':
        utext = request.POST.get('username')
        ptxt = request.POST.get('password')
        print(utext,ptxt)

        if utext != "" and ptxt != "":

            user = authenticate(username = utext, password = ptxt )

            if user != None:

                login(request,user)
                return redirect('profile')
    return render(request,'users/login.html',{"title":title})

def mylogout(request):
    logout(request)
    return redirect('mylogin')




def profile(request):
    #LOGIN CHECK CODE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #LOGIN CHECK ENDS

    transactiondetails = Transactiondata.objects.filter(sendername =request.user).all()
    transactiondetails_reversed = Transactiondata.objects.filter(recievername=request.user).all()
    mycoin = UsersData.objects.filter(username=request.user).get()
    title = Main.objects.get(pk=1)
    print(transactiondetails_reversed)

    return render(request,'users/userpage.html',{"title":title, 'mycoin':mycoin,'transactiondetails':transactiondetails,'transactiondetails_reversed':transactiondetails_reversed})


def userlist(request):
    #LOGIN CHECK CODE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #LOGIN CHECK ENDS
    title = Main.objects.get(pk=1)
    manager = UsersData.objects.all()

    return render(request,'users/list.html',{"title":title,"manager":manager})


def theqrcode(request):
    # LOGIN CHECK CODE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # LOGIN CHECK ENDS
    title = Main.objects.get(pk=1)
    return render(request, 'users/qrcode.html',{'title':title})
