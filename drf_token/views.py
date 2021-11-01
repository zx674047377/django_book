from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import exceptions
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_token.models import UserInfo, UserToken, CommonVideo, VIPVideo, SVIPVideo
from drf_token.serializers import CommonVideoSerializer, VIPVideoSerializer, SVIPVideoSerializer
from drf_token.utils.auth import Authentication, VIP, SVIP


def md5(user):
    import hashlib
    import time

    ctime = str(time.time())
    m = hashlib.md5(bytes(ctime, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


class AuthView(APIView):
    """登陆"""
    authentication_classes = []

    def post(self, request):
        ret = {'code': 1000, 'msg': '登录成功'}
        try:
            user = request.query_params.get("username")
            pwd = request.query_params.get("password")
            obj = UserInfo.objects.filter(username=user, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
                return JsonResponse(ret)
            token = md5(user)
            UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = "异常为:" + str(e)

        return JsonResponse(ret)


class CommonVideoView(APIView):
    """
    登录后即可访问的内容资源
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    authentication_classes = [Authentication, ]

    def get(self, request):
        video_list = CommonVideo.objects.all()
        re = CommonVideoSerializer(video_list, many=True)
        return Response(re.data)


class VIPVideoView(APIView):
    """vip可以访问的资源"""
    renderer_classes = [JSONRenderer]  # 渲染器
    permission_classes = [VIP, ]

    def get(self, request):
        video_list = VIPVideo.objects.all()
        re = VIPVideoSerializer(video_list, many=True)
        return Response(re.data)


class SVIPVideoView(APIView):
    """SVIP可以访问的资源"""
    renderer_classes = [JSONRenderer]  # 渲染器
    permission_classes = [SVIP, ]

    def get(self, request):
        video_list = SVIPVideo.objects.all()
        re = SVIPVideoSerializer(video_list, many=True)
        return Response(re.data)

