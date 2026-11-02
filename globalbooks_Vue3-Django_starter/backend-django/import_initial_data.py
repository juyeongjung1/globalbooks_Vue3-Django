"""マイグレーション後、空の書籍テーブルへ初期SQLを投入する。"""
import sqlite3
from pathlib import Path


def main():
    folder = Path(__file__).resolve().parent
    database = folder / 'db.sqlite3'
    if not database.exists():
        raise SystemExit('先にBookモデルを実装し、makemigrationsとmigrateを実行してください。')

    with sqlite3.connect(database) as connection:
        if connection.execute('SELECT COUNT(*) FROM books').fetchone()[0]:
            raise SystemExit('書籍が登録済みのため、初期データは投入しません。')
        sql = (folder / 'initial_data.sql').read_text(encoding='utf-8-sig')
        connection.executescript('BEGIN;\n' + sql + '\nCOMMIT;')
    print('初期データを10件登録しました。')


if __name__ == '__main__':
    main()
