from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList,Item,NewPost
from .forms import CreateNewList, CreateNewPost
from django.shortcuts import get_object_or_404

# Create your views here.

def welcome(response):
    return render(response,"main/welcome.html", {})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewPost(response.POST)
        if form.is_valid():
            tf = form.cleaned_data["textfield"]
            newForm = NewPost(textfield=tf, user=response.user)
            newForm.save()
    else:
        form = CreateNewPost()
    
    posts = NewPost.objects.all()  # Fetch all posts from the database

    return render(response, "main/create.html", {"form":form, "posts": posts})

def viewPost(response):
    posts = NewPost.objects.filter(user=response.user)
    return render(response,"main/viewPosts.html",{"posts": posts})

def deletePost(request, postID):
    post = get_object_or_404(NewPost, id=postID)
    if request.method == "POST":
        post.delete()
        return redirect('/viewPosts')
    return render(request, 'main/viewPosts.html', {'posts':post})



