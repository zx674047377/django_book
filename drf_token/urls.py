from django.urls import path

from drf_token.views import AuthView, CommonVideoView, VIPVideoView, SVIPVideoView

urlpatterns = [
    path('auth/', AuthView.as_view(), name="auth"),
    path('common/', CommonVideoView.as_view(), name="common"),
    path('vip/', VIPVideoView.as_view(), name="vip"),
    path('svip/', SVIPVideoView.as_view(), name="svip")
]
