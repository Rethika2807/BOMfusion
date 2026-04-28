from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import classify, mbom, routing, upload

app = FastAPI(title="eBOM → mBOM AI System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(classify.router, prefix="/api")
app.include_router(mbom.router, prefix="/api")
app.include_router(routing.router, prefix="/api")
app.include_router(upload.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "API Running 🚀"}