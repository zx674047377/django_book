from rest_framework import exceptions

from drf_token.models import UserToken


class Authentication:
    def authenticate(self, request):
        token = request.query_params.get("token")
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return token_obj.user, token_obj

    def authenticate_header(self, request):
        # 可以没有内容,但是必须有这个函数
        pass


class VIP:
    """
    VIP权限
    """

    def has_permission(self, request, view):
        if request.user.user_type < 2:
            return False
        return True


class SVIP:
    """SVIP权限"""

    def has_permission(self, request, view):
        if request.user.user_type < 3:
            return False
        return True
