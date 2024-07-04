from fastapi import FastAPI,Request
import models
from database import engine,SessionLocal
from Routes import items,dashboard
import re
from crud import log_api_request
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    config('FRONTEND_URL')
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

@app.middleware("http")
async def api_middleware(request : Request,call_next):
    db = SessionLocal()
    try:
        if not re.match(r"^/dashboard/.*", request.url.path):
            await log_api_request(request, db)
    finally:
        db.close()
    response =await call_next(Request)
    return response

app.include_router(items.router)
app.include_router(dashboard.router)
