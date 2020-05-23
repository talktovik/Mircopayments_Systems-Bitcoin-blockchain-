"""here we write query for example
we defined database already and now here we write the queries """

from django.shortcuts import render ,get_object_or_404 , redirect
from .models import Main , MainSub  #Main import kar liya h ab khel kar sakte h | aur ab main sub bhi kar liya


# Create your views here.

def home(request):
    title = Main.objects.get(pk =1) #query for class Main

    return render(request,'front/home.html', {"title":title})

def about(request): #this is the second page about.and we first create it because we want to have a looki over there.
    title = Main.objects.get(pk=1)
    return render(request,'front/about.html', {"title":title})

def contact(request):
    title = Main.objects.get(pk=1)
    return render(request,'front/contact.html', {"title":title})

#see the syntax of query
def work(request):

    var = MainSub.objects.get(pk = 1)  #get method actually here don't require for and endfor flooring it just like {{var.Proof_of_work}} and things done
    title = Main.objects.get(pk=1)
    return render(request,'front/howitwork.html', {'var': var, "title":title})

