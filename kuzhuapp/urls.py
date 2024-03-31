from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('signup/', views.signup , name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name="kuzhuapp/login.html"), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('', views.home , name='home'),
    path('add/', views.Addmember, name="Addmember"),
    path('updatemember/<id>', views.Updatemember, name="updatemember"),
    path('members/', views.listmember, name="listmember"),
    path('addemi/<id>', views.Addemi, name="Addemi"),
    path('memberlist/', views.Memberlist, name="Memberlist"),
    path('memberdashboard/<id>', views.Memberdashboard, name="Memberdashboard"),
    path('loandispurse/', views.loandispurse, name="loandispurse"),
    path('delete/<id>', views.delete_member, name="delete_member"),
]
