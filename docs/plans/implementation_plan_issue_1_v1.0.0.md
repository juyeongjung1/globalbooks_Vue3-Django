# 実装計画：編集画面への画像パスフォーム追加 (Issue #1) v1.0.0

frontendの編集画面（`EmployeeEditView.vue`）に画像パスのフォームを追加し、既存のロジックと連携させます。この修正は Issue #1 と紐付けて管理します。

## ユーザーレビューが必要な事項
> [!IMPORTANT]
> この修正は `issue-1-add-image-path-form` という名前の新ブランチで作業を行い、既存の main ブランチにプルリクエストを作成する形で進めます。

## 提案される変更

### [Component Name] frontend

#### [MODIFY] [EmployeeEditView.vue](file:///c:/work/vue3/globalbooks_Vue3-Django/frontend/src/views/EmployeeEditView.vue)

テンプレートの「勤務地」入力欄の後に、画像パス用の入力欄を追加します。

```diff
       <div class="mb-3">
         <label>勤務地</label>
         <input type="text" class="form-control" v-model="location_name">
       </div>
+      <div class="mb-3">
+        <label>写真パス (例: /images/1001.png)</label>
+        <input type="text" class="form-control" v-model="image_path">
+        <div class="form-text">※public/imagesフォルダ内のファイル名を指定してください</div>
+      </div>
       <button class="btn btn-primary">保存</button>
```

## 検証プラン

### 手動確認
1. 社員一覧から「編集」をクリックして編集画面へ遷移。
2. 画像パス入力欄が表示され、既存の値（あれば）がセットされていることを確認。
3. 画像パスを書き換えて「保存」をクリック。
4. 詳細画面に戻り、画像が正しく表示（またはパスが更新）されていることを確認。
