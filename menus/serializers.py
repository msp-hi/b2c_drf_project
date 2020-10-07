from rest_framework import serializers

from menus import models


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Menu
        fields = ('name','icon', 'url', 'component')

class MenuTypeSerializer(serializers.HyperlinkedModelSerializer):
    types = serializers.ReadOnlyField(source='types.id')
    class Meta:
        model = models.MenuTypes
        fields = ('name','types', 'url', 'component')


class MenuTypeItemSerializer(serializers.HyperlinkedModelSerializer):
    types = serializers.ReadOnlyField(source='types.id')
    class Meta:
        model = models.MenuTypeItem
        fields = ('name','types', 'url', 'image', 'component')
