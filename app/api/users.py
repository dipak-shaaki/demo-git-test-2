import logging
from fastapi import APIRouter
from app.services.user_service import get_user_by_id, list_users

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/{user_id}")
def get_user(user_id: str):
    logger.info(f"Fetching user {user_id}")

    user = get_user_by_id(user_id)

    return user


@router.get("/")
def get_all_users(role: str = "user"):
    logger.info(f"Listing users for role={role}")

    return list_users(role)