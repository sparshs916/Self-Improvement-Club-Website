from django.urls import path

from . import views

urlpatterns=[
    path("", views.welcome, name="welcome"),
    path("home/",views.home, name="home"),
    path("create/",views.create, name="create"),
    path("viewPosts/",views.viewPost, name="viewPosts"),
    path("deletePost/<int:postID>/", views.deletePost, name="deletePost"),
    path("editProfilePic/",views.editProfilePic, name="editProfilePic")
]