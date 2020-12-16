from src.controllers import *

app = FastAPI()

app.add_api_route('/', index)