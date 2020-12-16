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
    AFRO = bigquery_client.query(
        """
            SELECT date_reported, who_region,SUM(new_cases) as day, who_region as region  FROM COVID19.who where who_region = 'AFRO' group by date_reported, who_region order by date_reported;
        """
    )
    AMRO = bigquery_client.query(
        """
            SELECT date_reported, who_region,SUM(new_cases) as day, who_region as region  FROM COVID19.who where who_region = 'AMRO' group by date_reported, who_region order by date_reported;
        """
    )
    WPRO = bigquery_client.query(
        """
            SELECT date_reported, who_region,SUM(new_cases) as day, who_region as region  FROM COVID19.who where who_region = 'WPRO' group by date_reported, who_region order by date_reported;
        """
    )
    EMRO = bigquery_client.query(
        """
            SELECT date_reported, who_region,SUM(new_cases) as day, who_region as region  FROM COVID19.who where who_region = 'EMRO' group by date_reported, who_region order by date_reported;
        """
    )
    SEARO = bigquery_client.query(
        """
            SELECT date_reported, who_region,SUM(new_cases) as day, who_region as region  FROM COVID19.who where who_region = 'SEARO' group by date_reported, who_region order by date_reported;
        """
    )
    EURO = bigquery_client.query(
        """
            SELECT date_reported, who_region,SUM(new_cases) as day, who_region as region  FROM COVID19.who where who_region = 'EURO' group by date_reported, who_region order by date_reported;
        """
    )


    # クエリの実行結果をデータフレームに取得する
    df_AFRO = AFRO.to_dataframe()
    df_AMRO = AMRO.to_dataframe()
    df_WPRO = WPRO.to_dataframe()
    df_EMRO = EMRO.to_dataframe()
    df_SEARO = SEARO.to_dataframe()
    df_EURO = EURO.to_dataframe()
    
    labels = df["datdate_reportede"]
    datas_AFRO = [df_AFRO["date_reported"], df_AFRO["day"], df_AFRO["who_region"]]
    datas_AMRO = [df_AMRO["date_reported"], df_AMRO["day"], df_AMRO["who_region"]]
    datas_WPRO = [df_WPRO["date_reported"], df_WPRO["day"], df_WPRO["who_region"]]
    datas_EMRO = [df_EMRO["date_reported"], df_EMRO["day"], df_EMRO["who_region"]]
    datas_SEARO = [df_SEARO["date_reported"], df_SEARO["day"], df_SEARO["who_region"]]
    datas_EURO = [df_EURO["date_reported"], df_EURO["day"], df_EURO["who_region"]]


    return templates.TemplateResponse('index.html', {'request': request, 'datas_AFRO':datas_AFRO, 'datas_AMRO':datas_AMRO, 'datas_WPRO':datas_WPRO, 'datas_EMRO':datas_EMRO, 'datas_SEARO':datas_SEARO, 'datas_EURO':datas_EURO, 'labels':labels})

