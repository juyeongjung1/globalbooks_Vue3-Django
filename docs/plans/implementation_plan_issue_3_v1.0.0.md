# 実装計画：登録・編集画面のボタン余白の改善 (Issue #3) v1.0.0

新規登録画面と編集画面のボタン（保存/登録）の直前に余白を追加し、デザインを整えます。

## ユーザーレビューが必要な事項
> [!NOTE]
> Bootstrap のユーティリティクラス（`mt-4`）を使用して余白を調整します。

## 提案される変更

### [Component Name] frontend

#### [MODIFY] [NewEmployeeView.vue](file:///c:/work/vue3/globalbooks_Vue3-Django/frontend/src/views/NewEmployeeView.vue)
#### [MODIFY] [EmployeeEditView.vue](file:///c:/work/vue3/globalbooks_Vue3-Django/frontend/src/views/EmployeeEditView.vue)

両ファイルとも、ボタンに `mt-4` クラスを追加します。

```diff
-      <button class="btn btn-primary">登録</button>
+      <button class="btn btn-primary mt-4">登録</button>
```

## 検証プラン

### 手動確認
1. 新規登録画面を開き、ボタンと入力欄の間に適切な空間があることを確認。
2. 編集画面を開き、同様にボタンの余白を確認。
