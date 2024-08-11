from rest_framework import serializers
from .models import NanoLink


class NanoLinkSerailzer(serializers.ModelSerializer):
    nano_link = serializers.SerializerMethodField()

    class Meta:
        model = NanoLink
        fields = ['original_link', 'nano_link',
                  'acces_count', 'key', 'created']
