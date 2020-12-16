from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from starlette.templating import Jinja2Templates  # new
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED

from google.cloud import bigquery

app = FastAPI(
    title="ToDo App",
    description="FastAPIで作成するToDoアプリケーション",
    versions="0.9 beta"
)
bigquery_client = bigquery.Client()

security = HTTPBasic()


# new テンプレート関連の設定 (jinja2)
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env  # Jinja2.Environment : filterやglobalの設定用

def index(request: Request):
    #BigQueryにクエリを投げる
    query_job = bigquery_client.query(
        """
        SELECT
            *
        FROM 
            `COVID19.test`
        ORDER BY 
            DATE
        """
    )


    # クエリの実行結果をデータフレームに取得する
    df = query_job.to_dataframe()
    
    labels = df["date"]
    datas = [df["pcr_positive_daily"], df["pcr_tested_daily"], df["cases_total"], df["death_total"]]


    return templates.TemplateResponse('index.html', {'request': request, 'datas':datas, 'labels':labels})

