# from account.serializer import MerchUser
from django.contrib import admin
from django.urls import path
from .views import addproject, index, register, loggin, loggout, profile, show_project
# , register,signIn, signOut
# from .views import add_project,profile, profile_photo,project,rate_project,delete_project,MerchList, MerchUsers, LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
   
      path('login', loggin, name='login'),
      path('logout', loggout, name='logout'),
      path('register', register, name='register'),
      path('profile', profile, name='profile'),
      path('show_project/<id>', show_project, name='individual_project'),
      path('addproject', addproject, name='newproject'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
