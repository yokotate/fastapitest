from src.urls import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app=app)