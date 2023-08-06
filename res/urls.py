from django.urls import path, include
from .views import home,loginUser,register,about,rentalsavailable,contact,bill,payment,logoutuser,afterlogin,landing,feedback
urlpatterns = [

    path('home/', home,name="home"),
    path('login/', loginUser, name="login"),
    path('register/', register, name="register"),
    path('about/', about, name="about"),
    path('rentalsavailable/', rentalsavailable, name="rentalsavailable"),
    path('contact/', contact, name="contact"),
    path('bill/',bill,name="bl"),
    path('payment/',payment,name='db'),
    path('logout/', logoutuser, name='logout'),
    path('afterlogin/', afterlogin, name='afterlogin'),
    path('', landing, name='landing'),
    path('feedback/', feedback, name='feedback')

]
