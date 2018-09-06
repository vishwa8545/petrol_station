from django.conf.urls import url
from .views import Register,station
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    url(r'^register/',view=Register.as_view(),name='register' ),
    url(r'^station/',views.station),
    url(r'^login/',views.login_view),
    url(r'^update/',views.update),
    url(r'^$',views.index),
    ]
