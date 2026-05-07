import time
import logging

logger = logging.getLogger("request_logger")


def log_request(request, response):
    start = time.time()

    logger.info(
        f"REQUEST | path={request.url} | headers={request.headers} | body={getattr(request, 'body', None)}"
    )

    duration = time.time() - start

    logger.info(f"Response time: {duration}")