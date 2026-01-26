from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

# これだけで CRUD（一覧、詳細、登録、更新、削除）が全て完成します
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        # 1. まずは全件取得の準備
        queryset = Employee.objects.all()

        # 2. Vueから送られてきた 'keyword' パラメータを取得
        # (axiosの params: { keyword: ... } がここに入ります)
        keyword = self.request.query_params.get('keyword')

        # 3. キーワードが存在する場合のみ絞り込み (SQLの LIKE 検索に相当)
        if keyword:
            # 'name__icontains' は "name LIKE '%keyword%'" と同じ意味です
            # 'i' は ignore case (大文字小文字を区別しない) の意味
            queryset = queryset.filter(name__icontains=keyword)

        # 4. 結果を返す
        return queryset