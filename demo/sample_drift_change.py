# Demo file: changes the data-access pattern without updating .kiro/steering/review-standards.md
# Kiro should report steering drift on the "Data access" rule.
import logging
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent
from src.store.orders_store import OrdersStore  # new store layer replaces src/repo/ helpers

logger = logging.getLogger(__name__)
store = OrdersStore()


def handler(event: dict, context) -> dict:
    req = APIGatewayProxyEvent(event)
    logger.info("request", extra={"correlation_id": req.request_context.request_id})
    store.save(req.json_body)
    return {"statusCode": 201}
