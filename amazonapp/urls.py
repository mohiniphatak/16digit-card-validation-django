from django.conf.urls import url
from . import views
#. means current directory

urlpatterns = [
    url(r'^$',views.index),
    url(r'addorder',views.addorder),
]
