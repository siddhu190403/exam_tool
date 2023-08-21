from django.urls import path
from . import views

urlpatterns = [
    path('',views.helloDjango,name='helloworld'),
    path('search/',views.searchpage,name='searchpage'),
    path('login',views.LoginPage,name='login page'),
    path('sign-up/',views.SignupPage,name='sign-up page'),
    path('search/result/',views.result,name='result'),
    path('sign-up/register',views.register,name='register new user'),
    path('search/logout/',views.Logout,name='logout'),
    path('logout/',views.Logout,name='Logout'),
    path('search/result/history',views.ViewHistory,name='History')
 ]