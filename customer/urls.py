from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('accounts/sign_up/',views.sign_up,name="sign_up"),
    path('accounts/login/',views.loginview,name="login"),
    path('loginpage',views.loginpage,name="loginpage"),
    path('customerpage',views.customerpage,name="customerpage"),
    path('adding',views.adding,name="adding"),
    path('addcustomer',views.addcustomer,name="addcustomer"),
    path('updatename',views.updatename),
    path('updatephone',views.updatephone),
    path('editing',views.editing,name="editing"),
    path('updateaddress',views.updateaddress),
    path('updateemail',views.updateemail),
    path('feeding',views.feeding,name="feeding"),
    path('feedback1',views.feedback1,name="feedback1"),
    path('display',views.display,name="display"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('changepass',views.changepass,name="changepass")
]
