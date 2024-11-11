from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.register_user, name='user-register'),
    path("blog_list/", views.blog_list, name="blog_list"),
    path("blog_detail/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("create_blog/", views.create_blog, name="create_blog"),
    path("update_blog/<slug:slug>/", views.update_blog, name="update_blog"),
    path("delete_blog/<slug:slug>/", views.delete_blog, name="delete_blog"),
    path("user_info/<slug:username>", views.user_info, name="user_info"),
    path("get_username", views.get_username, name="get_username"),
    path("update_profile/", views.update_profile, name="update_profile")
]
