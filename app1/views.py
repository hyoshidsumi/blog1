from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView
from . import models


state_success = 200
state_error = 500

message_success = '正常に記録されました'
message1 = '記録に失敗しました'
message2 = '理由はよく分かりませんが、作った人に聞いて下さい'
message_error = [message1, message2]

ITEM_PER_PAGE = 9


def a(req):
    return render(req, 'signin.html', {'a': a})


def signupView(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('signin')
        except IntegrityError:
            message1 = '同じ名前の冒険者がいるようです'
            message2 = '別の名前で作成しましょう！'
            message = [message1, message2]
            return render(req, 'signup.html', {'error': message})

    else:
        return render(req, 'signup.html', {})


def signinView(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('home')
    return render(req, 'signin.html', {})


def signoutView(req):
    logout(req)
    return redirect('signin')


@login_required
def homeView(req):
    all = models.blogModel.objects.all()
    all_category = models.blogModel.objects.order_by('-category')
    all_user = models.blogModel.objects.order_by('-user')
    all_user = models.blogModel.objects.filter(user=req.user)
    print(all)
    pagenator = Paginator(all, ITEM_PER_PAGE)
    pp = req.GET.get('page', 1)
    page_list = pagenator.page(pp)
    print(page_list)
    range_pages = range(1, pagenator.num_pages+1)
    print(type(page_list))
    return render(req, 'home.html', {'object_list': all, 'page_list': page_list, 'range_pages': range_pages})


@login_required
def detailView(req, pk):
    object = models.blogModel.objects.get(pk=pk)
    return render(req, 'detail.html', {'object': object})


@login_required
def create(req):
    if req.method == 'POST':
        try:
            object = models.blogModel()
            object.title = req.POST['title']
            object.author = req.POST['author']
            object.user = req.user
            object.content = req.POST['content']
            if 'image' in req.FILES:
                object.blogImage = req.FILES['image']
            object.cdate = timezone.now()
            object.udate = timezone.now()
            object.save()
            print(message_success)
            return redirect('home')
        except:
            state = state_error
            print(message_error)
            return render(req, 'create.html', {'state': state, 'message': message_error})
    return render(req, 'create.html', {})


def deleteView(req, pk):
    try:
        object = models.blogModel.objects.get(pk=pk)
        object.delete()
        print(message_success)
        return redirect('home')
    except:
        print(message_error)
        return redirect('detail')


def updateView(req, pk):
    object = models.blogModel.objects.get(pk=pk)
    if req.method == "POST":
        print(req.POST)
        try:
            object.user = req.user
            object.title = req.POST['title']
            object.content = req.POST['content']
            if 'image' in req.FILES:
                object.blogImage = req.FILES['image']
            object.udate = timezone.now()
            object.save()
            print(message_success)
            return redirect('detail', pk=pk)
        except:
            print(message_error)
            return redirect('update', pk=pk)
    return render(req, 'update.html', {'object': object})
