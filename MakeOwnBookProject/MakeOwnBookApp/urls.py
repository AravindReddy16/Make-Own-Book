from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('mainPage/<str:page>/',views.mainPage,name='mainPage'),
    path('',views.basePage,name='basePage'),
    path('newPage/',views.newPage,name='newPage'),
    path('aboutPage/',views.aboutPage,name='aboutPage'),
    path('deletePage/<str:page>/',views.deletePage,name='deletePage'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='MakeOwnBookApp/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='MakeOwnBookApp/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='MakeOwnBookApp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='MakeOwnBookApp/password_reset_complete.html'), name='password_reset_complete'),
]