from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from menus import models, serializers


class MenuList(APIView):
    def get(self, request):
        queryset = models.Menu.objects.all()
        results = serializers.MenuSerializer(instance=queryset, many=True)
        return Response(results.data, status=status.HTTP_200_OK)


class MenuTypeList(APIView):
    def get(self, request, pk):
        queryset = models.MenuTypes.objects.filter(types=pk)
        results = serializers.MenuTypeSerializer(instance=queryset, context={'request':request}, many=True)
        return Response(results.data, status=status.HTTP_200_OK)
 

class MenuTypeItemList(APIView):
    def get(self, request, pk):
        queryset = models.MenuTypeItem.objects.filter(types=pk)
        results = serializers.MenuTypeItemSerializer(instance=queryset, context={'request':request}, many=True)
        return Response(results.data, status=status.HTTP_200_OK)
 
