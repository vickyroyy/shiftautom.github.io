from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index,name='home'),
    path("home",views.home,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("demo",views.demo,name='demo'),


    path('login',views.handleLogin,name="login"),
    path('logout',views.handleLogout,name="logout"),
    path('register',views.register,name="register"),
    path('signup',views.handlesignup,name="signup"),


   
]
