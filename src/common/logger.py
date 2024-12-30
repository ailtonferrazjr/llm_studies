import logging
import json
from datetime import datetime, timezone

class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "timestamp": self.get_now().isoformat(),  # Convert to ISO format string
            "level": record.levelname,
            "service": record.name,
            "message": record.getMessage()
        }

        return json.dumps(log_record)

    def get_now(self):
        return datetime.fromtimestamp(datetime.now().timestamp(), timezone.utc)


def get_logger(service_name: str) -> logging.Logger:
    """
    Get a configured logger for the specified service

    Args:
        service_name: Name of the service that will be logged (e.g., 'openai_service', 'summarizer')
    """

    logger = logging.getLogger(service_name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(JSONFormatter())
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger