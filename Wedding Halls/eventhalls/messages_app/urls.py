from django.urls import path
from . import views

urlpatterns = [
    path('chat-list/', views.chat_list, name='chat-list')
]