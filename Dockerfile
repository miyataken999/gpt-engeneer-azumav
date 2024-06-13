# ベースイメージとしてPython 3.9 slimを使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY requirements.txt requirements.txt

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# サーバーを起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
