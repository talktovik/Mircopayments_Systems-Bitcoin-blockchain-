from django.shortcuts import render, get_object_or_404 , redirect
from main.models import Main
from .models import Post
import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.

def blog(request):
    title = Main.objects.get(pk=1)
    allpost = Post.objects.all()

    return render(request,'blog/show.html',{'title':title,'allpost':allpost})

def add(request):    # data migration
    title = Main.objects.get(pk=1)
    allpost = Post.objects.filter()

    #date time addition thing
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)

    today = str(day) +"/" + str(month) + "/" + str(year)


    if request.method == 'POST':
        post_title = request.POST.get('ptitle')
        tag =  request.POST.get('tag')
        post = request.POST.get('post')

        if post_title == "" or tag == "" or post == "":
            error = "ALL FIELD REQUIRED"
            return render(request, 'blog/error.html', {'title': title, 'allpost': allpost,'error':error})

        b = Post(title = post_title,tag = tag, post = post,thetime = today,writer = request.user)
        b.save()
        return redirect('blog')



    return render(request,'blog/add.html',{'title':title,'allpost':allpost})


def function(request):
    response = "message: All good. The Blockchain is valid."
    return HttpResponse(response)




