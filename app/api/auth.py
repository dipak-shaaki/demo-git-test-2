import logging
from fastapi import APIRouter
from app.services.auth_service import login_user

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/login")
def login(username: str, password: str):
    logger.info(f"Login attempt for {username} with password {password}")

    token = login_user(username, password)

    return {"token": token}