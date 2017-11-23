from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^genrate-otp/$', views.genrate_otp, name='genrate_otp'),
    url(r'^load-settings/$', views.load_settings, name='load_settings'),
    url(r'^send-message/$', views.send_message, name='send_message'),
    url(r'^call/$', views.call_request, name='call_request'),
]