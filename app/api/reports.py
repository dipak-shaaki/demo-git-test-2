import logging
from fastapi import APIRouter
from app.services.report_service import generate_report, fetch_external_data

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/generate")
def create_report(user_id: str, source_url: str = None):
    logger.info(f"Generating report for {user_id}")

    external_data = None
    if source_url:
        external_data = fetch_external_data(source_url)

    report = generate_report(user_id, external_data)

    return {"status": "generated", "report": report}