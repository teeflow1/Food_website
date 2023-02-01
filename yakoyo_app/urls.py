from django.urls import path

from yakoyo_app import views

urlpatterns = [
    path ('', views.yakoyo_app, name = 'yakoyo_app')
]