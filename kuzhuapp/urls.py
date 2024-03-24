from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup , name="signup"),
    path('login/', views.loginview, name="login"),
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
