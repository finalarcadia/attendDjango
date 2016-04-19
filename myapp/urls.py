from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /myapp/
    url(r'^$', views.index, name='index'),
]