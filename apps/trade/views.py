from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from .serializers import ShopCartSerializer
from .models import ShoppingCart

class ShoppingCartViewset(viewsets.ModelViewSet):
    """
    购物车功能
    list:获取购物车详情
    create：加入购物车
    delete：删除购物记录
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    serializer_class = ShopCartSerializer
    lookup_field = "goods_id"
    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)