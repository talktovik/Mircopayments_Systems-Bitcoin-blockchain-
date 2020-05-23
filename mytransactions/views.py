"""here we write query for example
we defined database already and now here we write the queries """

from django.shortcuts import render ,get_object_or_404 , redirect
from main.models import Main
from django.contrib.auth.models import User
from users.models import UsersData
from .models import Transactiondata
import datetime
import random
from ipware import get_client_ip

# Create your views here.

def starttransaction(request):
    ip, is_routable = get_client_ip(request)
    myname = request.user
    title = Main.objects.get(pk=1)
    mycoin = UsersData.objects.filter(username = myname).get()
    thetimeanddate = datetime.datetime.now()



    if request.method == 'POST':
        recievername = request.POST.get("uname")

        if not User.objects.filter(username = recievername) or recievername == "" :
            error = "Username dosn't Exists ! Please have a look form the list"
            return render(request, 'blog/error.html', {'title': title,'error': error})



    return render(request,'mytransactions/start_transactions.html',{'title': title, 'recievername': recievername, 'mycoin':mycoin, 'ip':ip,'thetimeanddate':thetimeanddate})

def confirmation(request):
    ip, is_routable = get_client_ip(request)
    myname = request.user
    title =  Main.objects.get(pk=1)
    mycoin = UsersData.objects.filter(username=myname).get()
    present_user_balance = mycoin.vikcoin
    rand = random.randint(12345, 1000000)
    thetimeanddate = datetime.datetime.now()

    if request.method == 'POST':
        usertransferamount = request.POST.get("amount")
        thereciever = request.POST.get("thereciever")


        if not User.objects.filter(username = thereciever) or thereciever == "" :
            error = "Username dosn't Exists ! Please have a look form the list"
            return render(request, 'blog/error.html', {'title': title,'error': error})

        if usertransferamount == "" or usertransferamount == "0" :
            error = "Invalid Tranfer Request"
            return render(request, 'blog/error.html', {'title': title, 'error': error})

        if int(usertransferamount) >= present_user_balance:
            error = "You dont have enough coins in your wallet please update it via requesting admin"
            return render(request, 'blog/error.html', {'title': title, 'error': error})

        remaining_amount = present_user_balance - int(usertransferamount)
        print(remaining_amount)



    b = Transactiondata(transactionid=rand, sendername=request.user, recievername=thereciever,
                        coin=present_user_balance, ipaddress=ip, timeanddate=thetimeanddate, transferamount=usertransferamount)
    b.save()

    UsersData.objects.filter(username=request.user).update(vikcoin = remaining_amount)
    reciever_current_balance_query = UsersData.objects.filter(username=thereciever).get()
    reciever_current_balance = reciever_current_balance_query.vikcoin
    credited_data = int(reciever_current_balance) + int(usertransferamount)
    UsersData.objects.filter(username = thereciever).update(vikcoin =credited_data)

    return render(request,'mytransactions/confirmation.html', {'title':title, 'thereciever':thereciever,'thetimeanddate':thetimeanddate,'ip':ip,'rand':rand,'usertransferamount':usertransferamount})