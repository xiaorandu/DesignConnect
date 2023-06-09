from rest_framework import status
from rest_framework.decorators import action  # 自定义的 api 动作需要用
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from inbox.services import NotificationService
from likes.api.serializers import (LikeSerializer, LikeSerializerForCancel,
                                   LikeSerializerForCreate)
from likes.models import Like
from utils.decorators import required_params


class LikeViewSet(GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializerForCreate
    permission_classes = [IsAuthenticated, ]

    # 这里是 post 方法, 这里参数用 data
    @required_params(method='POST', params=['content_type', 'object_id'])
    def create(self, request, *args, **kwargs):
        serializer = LikeSerializerForCreate(
            data=request.data,
            context={'request': request},
        )
        if not serializer.is_valid():
            return Response({
                'message': 'Please check input',
                'errors': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
        # instance = serializer.save() # 这里被 get_or_create方法取代了
        # 因为如果用户已经点赞过, 就不会重复发送通知, 所以我们需要获得 created的信息
        # created 表示之前没有点赞过, 是这次点赞的, 创建了一个 like 对象
        instance, created = serializer.get_or_create()
        if created:
            NotificationService.send_like_notification(instance)  # 点赞后发送通知
        return Response(
            LikeSerializer(instance).data,
            status=status.HTTP_201_CREATED
        )

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated])
    @required_params(method='POST', params=['content_type', 'object_id'])
    def cancel(self, request, *args, **kwargs):
        serializer = LikeSerializerForCancel(
            data=request.data,
            context={"request": request},
        )
        if not serializer.is_valid():
            return Response({
                'message': 'Please check input',
                'error': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)

        deleted = serializer.cancel()
        return Response({
            'success': True,
            'deleted': deleted,   # 可以知道是找到了再删除, 还是没有找到就删除了
        }, status=status.HTTP_200_OK)
