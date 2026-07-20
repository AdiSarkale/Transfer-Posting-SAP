from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware as CORS
import uvicorn
import httpx


from api import testApi

title = 'Material Transfer Posting'
app = FastAPI(title=title)

app.add_middleware(
    CORS,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(testApi.router)

@app.get('/')
def health():

    return {
        'title' : title,
        'live' : True
        }





if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
