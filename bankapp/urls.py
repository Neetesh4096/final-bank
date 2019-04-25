
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('home/', include('myapp.urls')),
    path('login/', include('myapp.urls')),
    path('signup/', include('myapp.urls')),
    path('contact/', include('myapp.urls')),
    path('loginsuccess/', include('myapp.urls')),
    path('credit/', include('myapp.urls')),
    path('debit/', include('myapp.urls')),
    path('logout/', include('myapp.urls')),
    path('chk_bal/', include('myapp.urls')),
    path('edit_profile/', include('myapp.urls')),
    path('mkcredit/', include('myapp.urls')),
    path('about/', include('myapp.urls')),

]
