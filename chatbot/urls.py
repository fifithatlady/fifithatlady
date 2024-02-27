from django.urls import path
from chatbot.views import chatbot

app_name = 'chatbot'

urlpatterns = [
    path('', chatbot, name='chatbot'),
]
