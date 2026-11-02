"""受講者用ファイルだけをZIPにまとめる（Python標準ライブラリのみ）。"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import os


root = Path(__file__).resolve().parents[1]
starter = root / 'globalbooks_Vue3-Django_starter'
output = root / 'output' / 'globalbooks_starter_v1.1.0.zip'
excluded_dirs = {'.git', '.venv', 'node_modules', 'dist', '__pycache__', '.vscode'}

output.parent.mkdir(exist_ok=True)
with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
    for folder, dirs, files in os.walk(starter):
        dirs[:] = sorted(name for name in dirs if name not in excluded_dirs)
        for name in sorted(files):
            path = Path(folder) / name
            # 指示の原本PDFは手元に保持し、配布には更新済みREADMEを使う。
            if name == 'README (1).pdf' or path.suffix in {'.pyc', '.pyo', '.sqlite3', '.db'}:
                continue
            archive.write(path, Path(starter.name) / path.relative_to(starter))
print(f'配布用ZIPを作成しました: {output}')
