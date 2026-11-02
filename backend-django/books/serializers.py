from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # 価格は1以上の整数にする（登録・更新で共通）。
        extra_kwargs = {'price': {'min_value': 1}}
