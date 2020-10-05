from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from goods import models, seralizers


class GoodsTypeList(APIView):
    def get(self, request):
        goods_type_list = models.GoodsType.objects.all()
        goods_type_data = seralizers.GoodsTypeSerializer(instance=goods_type_list, many=True)
        return Response(goods_type_data.data, status=status.HTTP_200_OK)


class GoodsTypeMenuList(APIView):
    def get(self, request):
        goods_class_list = models.GoodsTypeMenu.objects.all()
        gooods_class_data = seralizers.GoodsTypeMenuSerializer(instance=goods_class_list, context={'request':request}, many=True)
        return Response(gooods_class_data.data, status=status.HTTP_200_OK)