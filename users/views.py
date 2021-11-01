from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import UserProfile, Book
from users.serializers import BookSerializer, BookModelSerializer


class BooKAPIView1(APIView):
    """使用serializer"""

    def get(self, request, format=None):
        APIKey = self.request.query_params.get("apikey", 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()

        if developer:
            balance = developer.money
            if balance > 0:
                isbn = self.request.query_params.get("isbn", 0)
                books = Book.objects.filter(isbn=int(isbn))
                # instance接受queryset对象或者单个model对象，当有多条数据时候，使用many=True,单个对象many=False
                books_serializer = BookSerializer(books, many=True)
                developer.money -= 1
                developer.save()

                return Response(books_serializer.data)

            else:
                return Response("余额不足")

        else:
            return Response("没有这个信息!")


class BookAPIView2(APIView):

    def get(self, request, format=None):
        APIKey = self.request.query_params.get("apikey", 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()

        if developer:
            balance = developer.money
            if balance > 0:
                isbn = self.request.query_params.get("isbn", 0)
                books = Book.objects.filter(isbn=int(isbn))
                # instance接受queryset对象或者单个model对象，当有多条数据时候，使用many=True,单个对象many=False
                books_serializer = BookModelSerializer(books, many=True)
                developer.money -= 1
                developer.save()

                return Response(books_serializer.data)

            else:
                return Response("余额不足")

        else:
            return Response("没有这个信息!")


from rest_framework import mixins, viewsets
from rest_framework import generics


class BookMixinView1(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request, *args, **kwargs):  # 如果这里不加get函数，代表默认不
        # 支持get访问这个api，所以必须加上
        APIKey = self.request.query_params.get("apikey", 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            balance = developer.money
            if balance > 0:
                isbn = self.request.query_params.get("isbn", 0)
                developer.money -= 1
                developer.save()
                self.queryset = Book.objects.filter(isbn=int(isbn))
                return self.list(request, *args, **kwargs)
            else:
                return Response("兄弟，又到了需要充钱的时候！好开心啊！")
        else:
            return Response("查无此人啊")


class IsDeveloper(BasePermission):
    message = "查无此人啊"

    def has_permission(self, request, view):
        APIKey = request.query_params.get("apikey", 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            return True
        else:
            print(self.message)
            return False


class EnoughMoney(BasePermission):
    message = "没钱了,充值吧"

    def has_permission(self, request, view):
        APIKey = request.query_params.get("apikey", 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        balance = developer.money
        if balance > 0:
            developer.money -= 1
            developer.save()
            return True
        else:
            print(self.message)
            return False


class BookModelViewSet(viewsets.ModelViewSet):
    authentication_classes = []  # 虽然没有认证 但是不加就没有自定义的message显示
    permission_classes = [IsDeveloper, EnoughMoney]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get_queryset(self):
        isbn = self.request.query_params.get("isbn", 0)
        books = Book.objects.filter(isbn=int(isbn))
        return books
