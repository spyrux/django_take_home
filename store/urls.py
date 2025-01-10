from django.urls import path

from . import views

urlpatterns = [
    path("", views.StoreListView, name="StoreListView"),
]