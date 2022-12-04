from django.urls import path
from django.conf.urls import url
from app import views
from django.views.generic import TemplateView

urlpatterns = [
  path('',views.index,name='index'),
  path('About',views.About,name='About'),
  path('Home',views.Home,name='Home'),
  path('contact',views.contact,name='contact'),
  path('base',views.base,name='base'),
  path('signin',views.signin,name='signin'),
  path('Register',views.Register,name='Register'),
  path('loan',views.loan,name='loan'),
  path('next',views.next,name='next'),
  path('next2',views.next2,name='next2'),
  path('next3',views.next3,name='next3'),
  path('next4',views.next4,name='next4'),
  path('next5',views.next5,name='next5'),
  path('next6',views.next6,name='next6'),
  path('feedback',views.feedback,name='feedback'),
  path('logout', views.handelLogout, name="handleLogout"),
  

]

