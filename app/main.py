from fastapi import FastAPI
from app.api.auth import router as auth_router
# from app.api.users import router as users_router
# from app.api.reports import router as reports_router

app = FastAPI(title="Internal Analytics Service")


@app.get("/")
def home():
    return {"status": "running"}


app.include_router(auth_router, prefix="/auth")
# app.include_router(users_router, prefix="/users")
# app.include_router(reports_router, prefix="/reports")