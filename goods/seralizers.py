from rest_framework import serializers

from goods import models


class GoodsTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.GoodsType
        fields = ('name', 'url', 'component')

class GoodsTypeMenuSerializer(serializers.HyperlinkedModelSerializer):
    types = serializers.ReadOnlyField(source='types.id')
    class Meta:
        model = models.GoodsTypeMenu
        fields = ('name','types', 'url', 'image', 'component')