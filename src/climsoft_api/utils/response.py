import math
from typing import List, Any


def get_success_response(result: List[Any], message: str):
    return {"status": "success", "message": message, "result": result}


def get_success_response_for_query(limit: int, total: int, offset: int, result: List[Any], message: str):
    return {
        "status": "success",
        "message": message,
        "limit": limit,
        "pages": math.ceil(total/limit),
        "page": math.floor(offset/limit)+1,
        "result": result
    }


def get_error_response(message: str, result: List[Any] = None):
    return {
        "status": "error",
        "message": message,
        "result": [] if result is None else result,
    }
