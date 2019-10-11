from django.urls import path

from . import views

urlpatterns = [path("", views.MenuItemListView.as_view(), name="menu-list-view")]
