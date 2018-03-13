from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(requset):
    """注册新用户"""
    if requset.method != 'POST':
        # 显示新的注册表单
        form = UserCreationForm
    else:
        # 处理填好的表单
        form = UserCreationForm(data=requset.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username=new_user.username, password=requset.POST['password1'])
            login(requset, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(requset, 'users/register.html', context)
