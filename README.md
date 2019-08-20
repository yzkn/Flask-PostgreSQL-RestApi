# Flask-RestApi

---

## 必要なパッケージのインストール

```sh
$ sudo apt-get install -y python3 python3-venv

$ python3 -m venv flaskrestapienv
$ . flaskrestapienv/bin/activate
# $ flaskrestapienv\Scripts\activate # Windowsの場合

$ pip install flask flask_cors SQLAlchemy psycopg2 flask-sqlalchemy Flask-Migrate
   or
$ pip install -r requirements.txt

# $ pip freeze > requirements.txt
```

## データベースの準備

```sh
# 一旦localhostで試行
$ psql -h localhost -p 5432 -U postgres -d postgres
> CREATE DATABASE dbrestapi ;
> \l
> CREATE ROLE userrestapi WITH LOGIN PASSWORD 'Passw0rd' ;
> \du
> GRANT ALL ON DATABASE dbrestapi TO userrestapi ;

$ psql -h localhost -p 5432 -U postgres -d postgres
> SELECT * FROM pg_database;

$ psql -h localhost -p 5432 -U userrestapi -d postgres
> SELECT * FROM pg_database;
```

## データベースのマイグレーションとサーバの起動

```sh
$ FLASK_APP=run.py flask db init # migrationsフォルダ、ファイルを作成
$ FLASK_APP=run.py flask db migrate # modelクラスの定義の差分からmigrationファイルを作成
$ flask db upgrade # migrationを実行
# $ flask db downgrade # ロールバック
```

```powershell
# Windows(PowerShell)の場合
$ $env:FLASK_APP="run.py"
$ py -m flask db init
$ py -m flask db migrate
$ py -m flask db upgrade
```

## データベースのマイグレーションとサーバの起動

```sh
$ python run.py
```

```powershell
$ py run.py
```

---

# Copyright (c) 2019 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.
