"""mywork URL Configuration

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
from django.urls import path
from common.views import Connection
#from allauth.account.views import confirm_email
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from allauth.account.views import confirm_email
from member.views import Auth
from django.contrib import admin
# from member.views import MemberViewSet
# from board import views
router = routers.DefaultRouter()
# router.register(r'member', views.MemberViewSet)
# router.register(r'board', views.BoardViewSet)

urlpatterns = [
    path('connection', Connection.as_view()),
    path('board', include('board.urls')),
    url(r'^member/', include('member.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),

]
