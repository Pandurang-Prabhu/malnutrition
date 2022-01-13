"""Malnutrition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MalnutritionApp.views import index, save_report, user, registration,saveUser,userlogin,addReport,\
    logout,view_report,report_analysis,get_analysis_result,user_home,forgot_password,get_password,update_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('user/',user),
     path('user-home/',user_home),
    path('logout/', logout),
    path('registration/',registration),
    path('saveUser/',saveUser),
    path('userlogin/',userlogin),
    path('addReport/',addReport),
    path('save-report/',save_report),
    path('my-report/',view_report),
    path('report-analysis/',report_analysis),
    path('forgot-password/', forgot_password),
    path('get-password/', get_password),
    path('update-user/', update_login),
    path('get-analysis-result/<int:reportid>/<gender>/<infection>/<height>/<weight>/<hair>/<skin>/<stomach>/',get_analysis_result),
]
