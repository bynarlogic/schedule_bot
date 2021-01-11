from django.conf.urls import url
from schedule_bot.chatbot.views import ChatBotApiView

urlpatterns = [
    url(r'^api/chatbot/', ChatBotApiView.as_view(), name='chatbot')
]
