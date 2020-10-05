from rest_framework import serializers

from goods import models


class GoodsTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.GoodsType
        fields = ('id', 'name')

class GoodsTypeMenuSerializer(serializers.HyperlinkedModelSerializer):
    types = serializers.ReadOnlyField(source='types.id')
    class Meta:
        model = models.GoodsTypeMenu
        fields = ('id', 'name','types', 'url', 'image')