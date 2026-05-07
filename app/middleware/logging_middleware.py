import logging

logger = logging.getLogger("request_logger")


def log_request(user, request_data):
    logger.info(f"REQUEST | user={user} | data={request_data}")