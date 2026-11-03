from uuid import uuid4

from django.core.files.storage import default_storage
from django.db.models import F
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer, ImageUploadSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.query_params.get('keyword', None)
        if keyword:
            queryset = queryset.filter(title__icontains=keyword)
        # オプション1: 検索結果に対して、選択された順序を適用する。
        ordering = self.request.query_params.get('ordering', 'id')
        if ordering not in ['id', '-id', 'price', '-price', 'title', '-title', '-like_count']:
            ordering = 'id'
        return queryset.order_by(ordering, 'id')

    # オプション2: DB内の現在値に1を加える。
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        book = self.get_object()
        Book.objects.filter(pk=book.pk).update(like_count=F('like_count') + 1)
        book.refresh_from_db()
        return Response(self.get_serializer(book).data)

    # オプション3: 画像を保存し、既存のimage_pathで使えるURLを返す。
    @action(detail=False, methods=['post'], url_path='upload-image',
            parser_classes=[MultiPartParser], serializer_class=ImageUploadSerializer)
    def upload_image(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image = serializer.validated_data['image']
        extension = '.jpg' if image.image.format == 'JPEG' else '.png'
        filename = default_storage.save(f'books/{uuid4().hex}{extension}', image)
        image_path = request.build_absolute_uri(default_storage.url(filename))
        return Response({'image_path': image_path}, status=status.HTTP_201_CREATED)
