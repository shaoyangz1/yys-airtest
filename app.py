import uvicorn
from fastapi import FastAPI
from airtest.core import api

from settings import settings

app = FastAPI(title="阴阳师自动化脚本", version="1.0.0")


@app.on_event("startup")
async def init_app():
    api.init_device(uuid=settings.UUID)


@app.post(path="/exec", tags=["root"])
async def auto_exec():
    return {"message": "Hello World."}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081, workers=4)
