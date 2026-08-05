from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
import uvicorn

from api import testApi

BASE_DIR = os.path.dirname(__file__)
STATIC_FOLDER = os.path.join(BASE_DIR, "static")

app = FastAPI(title="Material Transfer Posting")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(testApi.router)

# Serve JS/CSS/assets
app.mount(
    "/assets",
    StaticFiles(directory=os.path.join(STATIC_FOLDER, "assets")),
    name="assets",
)


@app.get("/")
def index():
    return FileResponse(os.path.join(STATIC_FOLDER, "index.html"))


@app.get("/{path:path}")
def spa(path: str):
    file_path = os.path.join(STATIC_FOLDER, path)

    if os.path.exists(file_path):
        return FileResponse(file_path)

    return FileResponse(os.path.join(STATIC_FOLDER, "index.html"))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
