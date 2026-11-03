from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['like_count']
        # 価格は1以上の整数にする（登録・更新で共通）。
        extra_kwargs = {'price': {'min_value': 1}}


class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()

    def validate_image(self, image):
        if image.size > 5 * 1024 * 1024:
            raise serializers.ValidationError('画像は5MB以下にしてください。')
        if image.image.format not in ['JPEG', 'PNG']:
            raise serializers.ValidationError('JPEGまたはPNG画像を選択してください。')
        return image
