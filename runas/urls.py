from django.conf.urls import url

from .views import runas_enter, runas_exit

app_name = 'runas'
urlpatterns = [
    url('^enter/(?P<user_id>\d+)$', runas_enter, name='enter'),
    url('^exit$', runas_exit, name='exit'),
]
