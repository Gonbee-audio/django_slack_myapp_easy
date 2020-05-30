from django.urls import path
from slack.views import SingUpAccount, Login, ChatModel, SendChatMessage

urlpatterns = [
    path('SignUp/', SingUpAccount, name="signup"),
    path('Login/', Login, name="login"),
    path('Chat/', ChatModel, name="chat"),
    path('ChatSend/', SendChatMessage, name="sendchatmessage")
]