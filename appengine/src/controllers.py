from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from starlette.templating import Jinja2Templates  # new
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED

import hashlib, secrets, re

app = FastAPI(
    title="ToDo App",
    description="FastAPIで作成するToDoアプリケーション",
    versions="0.9 beta"
)

security = HTTPBasic()


# new テンプレート関連の設定 (jinja2)
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env  # Jinja2.Environment : filterやglobalの設定用

def index(request: Request):
    return templates.TemplateResponse('./contents/index.html', {'request': request})
