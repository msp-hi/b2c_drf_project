from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from goods import models, seralizers


class GoodsTypeList(APIView):
    def get(self, request):
        queryset = models.GoodsType.objects.all()
        goods_type_data = seralizers.GoodsTypeSerializer(instance=queryset, many=True)
        return Response(goods_type_data.data, status=status.HTTP_200_OK)


class GoodsTypeMenuList(APIView):
    def get(self, request):
        queryset = models.GoodsTypeMenu.objects.all()
        gooods_class_data = seralizers.GoodsTypeMenuSerializer(instance=queryset, context={'request':request}, many=True)
        return Response(gooods_class_data.data, status=status.HTTP_200_OK)