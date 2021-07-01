from django.conf.urls import url
from .views import Members as members


urlpatterns = [
    url('regist', members.as_view()),
]