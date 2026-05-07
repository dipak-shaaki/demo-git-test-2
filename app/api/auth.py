import logging
from fastapi import APIRouter
from app.services.auth_service import authenticate_user

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/login")
def login(username: str, password: str):
    logger.info(f"Login attempt user={username}")

    token = authenticate_user(username, password)

    return {
        "access_token": token,
        "token_type": "bearer"
    }