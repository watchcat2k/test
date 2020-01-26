from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
import json

# Create your views here.
# 注意data字段，因为__ok__是全局变量，所以每次返回时都要对data进行赋值，以覆盖原来的data值

__ok__ = {
    'code': 200,
    'message': 'OK',
    'data': {}
}

__error__ = {
    'code': 400,
    'message': '服务器发生错误'
}

__notExistUser__ = {
    'code': 400,
    'message': '用户名不存在'
}

__hasExistUser__ = {
    'code': 400,
    'message': '用户名已存在'
}

__wrongPassword__ = {
    'code': 400,
    'message': '密码错误'
}

__notLogin__ = {
    'code': 401,
    'message': '用户未登录'
}


@csrf_exempt
def video_index(request):
    return HttpResponse("This is video index")


@csrf_exempt
def user_register(request):
    """用户注册"""
    try:
        if request.method == 'POST':
            parameters = request.POST
            # 获取多个对象用filter
            filter_user = models.User.objects.filter(
                user_username=parameters['username'])
            if filter_user.__len__() == 0:
                new_user = models.User(
                    user_username=parameters['username'],
                    user_password=parameters['password'],
                    user_name=parameters['name'],
                )
                new_user.save()
                # session保存用户登录状态
                request.session['user_id'] = new_user.user_id
                request.session['is_login'] = True
                data = {}
                __ok__['data'] = data
                return HttpResponse(json.dumps(__ok__), content_type='application/json', charset='utf-8')
            else:
                return HttpResponse(json.dumps(__hasExistUser__), content_type='application/json', charset='utf-8')
    except Exception as exc:
        print(exc)
        return HttpResponse(json.dumps(__error__), content_type='application/json', charset='utf-8')


@csrf_exempt
def user_avatar(request):
    """修改用户头像"""
    try:
        if request.method == 'POST':
            avatar = request.FILES.get('avatar')
            fname = 'D:\\user_chen\\my_home_page\\files\\' + '2020-1-22-1'
            with open(fname, 'wb') as pic:
                for c in avatar.chunks():
                    pic.write(c)
            print(fname)
    except Exception as exc:
        print(exc)
        return HttpResponse(json.dumps(__error__), content_type='application/json', charset='utf-8')
