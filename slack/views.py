from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from slack.models import ChatMessage
from slack.forms import PostChatMessage
from django.contrib.auth import authenticate, login
# Create your views here.

def SingUpAccount(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']
        try:
            User.objects.get(username=username1)
            return render(request, 'SignUp.html', {'error':'この名前は既に使われています'})
        except:
            User.objects.create_user(username1, '', password1)
            return render(request, 'Login.html', {})
    return render(request, 'SignUp.html', {})

def Login(request):
    if request.method == "POST":
        LoginUsername = request.POST['username']
        LoginPassword = request.POST['password']
        LoginUserInformation = authenticate(username=LoginUsername, password=LoginPassword)
        if LoginUserInformation is not None:
            login(request, LoginUserInformation)
            return redirect('chat')
        else:
            return render(request, 'Login.html', {})
    return render(request, 'Login.html', {})

def SendChatMessage(request):
    form = PostChatMessage()
    if request.method == 'POST':
       form = PostChatMessage(request.POST)
       if form.is_valid():
           post = form.save(commit=True)
           post.save()
           return redirect('chat')
       else:
           form = PostChatMessage()
           return render(request, 'redirect', {})
    return render(request, 'ChatSend.html', {'form':form})

def ChatModel(request):
    object = ChatMessage.objects.all()
    return render(request, 'Chat.html', {'object':object}) 

