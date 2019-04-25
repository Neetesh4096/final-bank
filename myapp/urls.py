
from django.urls import path
from . import views
urlpatterns= [
    path("",views.index,name='home'),
    path('home/', views.home),
    path('login/', views.Login),
    path('signup/', views.Signup),
    path('contact/', views.contact),
    path('loginsuccess/', views.loginsuccess),
    path('mksignup/', views.mksignup),
    path('credit/', views.credit),
    path('mkcredit/', views.mkcredit),
    path('debit/', views.debit),
    path('mkdebit/', views.mkdebit),
    path('chk_bal/', views.chk),
    path('about/', views.about),

    ]