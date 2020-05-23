from django.shortcuts import render, get_object_or_404 , redirect
from main.models import Main
from mytransactions.models import Transactiondata
from users.models import UsersData
from blockchain.models import Thelongestchain

import datetime
from django.contrib.auth.models import User

def panel(request):
    transactiondetails = Transactiondata.objects.filter().all()

    title = Main.objects.get(pk=1)
    coin = Transactiondata.objects.all()
    total_coin =0
    for i in coin:
        total_coin = total_coin + i.transferamount




    return render(request,'thepanel/index.html',{'title':title,'total_coin':total_coin,'transactiondetails':transactiondetails})

def panellist(request):
    title = Main.objects.get(pk=1)
    manager = UsersData.objects.all()
    totaluser = UsersData.objects.filter().count()  # count things
    return render(request,'thepanel/viklist.html',{'totaluser':totaluser,'manager':manager,'title':title})


def vikblock(request):
    title = Main.objects.get(pk=1)
    thevar = Thelongestchain.objects.filter().order_by('-id')[0]
    theblocknumber = thevar.id
    blocks = Thelongestchain.objects.all()
    return render(request,'thepanel/vikblocks.html',{'title':title,'blocks':blocks,'theblocknumber':theblocknumber})

# def num_post(request):
#     num_post = Post.objects.filter(author=request.user).count()
#     return render(request, 'some_template.html', {'num_post': num_post})