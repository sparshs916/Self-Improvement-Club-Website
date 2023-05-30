from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import NewPost
from .forms import CreateNewList, CreateNewPost
from register.models import UserProfile
from django import http

# Create your views here.

def welcome(response):
    return render(response,"main/welcome.html", {})

def home(request):
   return create(request)

def create(request):
    if request.method == "POST":
        form = CreateNewPost(request.POST)
        if form.is_valid():
            try:
                profile = UserProfile.objects.get(user=request.user)
            except:
                profile = None
            tf = form.cleaned_data["textfield"]
            newForm = NewPost(textfield=tf, user=request.user)
            newForm.save()
    else:
        profile = None
        form = CreateNewPost()
    posts = NewPost.objects.all().order_by('-created_at')

    return render(request, "main/home.html", {"form":form, "posts": posts, "profile":profile})


def viewPost(request):
    posts = NewPost.objects.filter(user=request.user)
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    posts = NewPost.objects.all().order_by('-created_at')
    return render(request,"main/viewPosts.html",{"posts": posts,"profile":profile})

def deletePost(request, postID):
    post = get_object_or_404(NewPost, id=postID)
    if request.method == "POST":
        post.delete()
        return redirect('viewPosts')
    return render(request, 'main/viewPosts.html', {'posts':post})

def getProfilePic(request):
    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        return render(request,'main/viewPosts.html',{'profile':profile} )

def editProfilePic(request):
    profile = UserProfile.objects.get(user=request.user)
    posts = NewPost.objects.filter(user=request.user)
    if request.method == "POST":
        if "image" in request.FILES:
            image = request.FILES['image']
            profile.profileImage = image
            profile.save()
            return redirect('viewPosts')
    else:
         profile = UserProfile.objects.create(profile=image)
         profile.save()
         return redirect('viewPosts')
    context= {
        'profile':profile,
        'posts':posts
    }
    return render(request,'main/viewPosts.html',context )


'''def editProfilePic(request):
    profile = UserProfile.objects.get(user=request.user)
    posts = NewPost.objects.filter(user=request.user)
    if request.method == "POST":
        if 'image' in request.POST:
            form = UserProfile(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
        else:
            form = UserProfile()
    context= {
        'profile':profile,
        'posts':posts,
        'form':form
    }
    return render(request,'main/viewPosts.html',context )'''