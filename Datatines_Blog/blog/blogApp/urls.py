from django.urls import path
from . import views

app_name = 'blogApp'

urlpatterns = [
    path('', views.index, name="index"),
    path('ourBlog/', views.blog, name='blog'),
    path('seacrh',views.search_post,name='search'),
    path('post/<int:pk>/', views.Post.as_view(), name='showPost'),
    path('subscribe/',views.contactMail,name='subscribe'),
    path('login',views.adminLogin,name='login'),
    path('logout',views.user_logout,name='logout'),
]
