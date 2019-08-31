from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('create_message/', views.create_message_view),
    path('read_message/', views.read_message_view),
    path('delete_message/', views.delete_message_view),
    path('get_messages_by_user/', views.get_messages_by_user_view),
    path('get_unread_messages_by_user/', views.get_unread_messages_by_user_view),
]
