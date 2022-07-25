from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path('profile/', views.profile, name='profile'), 
    path('', views.index, name='index'),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
    path('print/', views.print, name='print'),
    path('transaction/<str:id>/', views.transaction, name='transaction'),
    path('signup/', views.signupform, name='signupform'),
    path('login/', views.loginfunc, name='login'),
    path('logout/', views.logoutfunc, name='logout'),
    path('pay/', views.pay, name='pay'),
 
]