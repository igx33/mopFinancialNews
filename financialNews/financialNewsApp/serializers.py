from rest_framework import serializers
from financialNewsApp.models import News, Symbol


class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = ['id', 'short_name', 'full_name', ]


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'symbol', 'description', 'original_guid', 'link', 'pub_date', 'title', 'created_date', ]
        depth = 1
