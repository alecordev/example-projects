import fastapi
import uvicorn

from views import home
from api import weather_api

api = fastapi.FastAPI()


def configure():
    api.include_router(home.router)
    api.include_router(weather_api.router)


configure()

if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000)
