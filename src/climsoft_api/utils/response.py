import json
import math
from typing import List, Any, Dict
from itertools import chain
import copy


def get_current_and_total_pages(limit: int, total: int, offset: int):
    return math.floor(offset / limit) + 1, math.ceil(total / limit)


def get_success_response(
    result: List[Any],
    message: str,
    schema: Any = None
):
    return {
        "status": "success",
        "message": message,
        "result": result,
        "_schema": schema
    }


def get_success_response_for_query(
    limit: int,
    total: int,
    offset: int,
    result: List[Any],
    message: str,
    schema: Any = None
):
    return {
        "status": "success",
        "message": message,
        "limit": limit,
        "pages": math.ceil(total / limit),
        "page": math.floor(offset / limit) + 1,
        "result": result,
        "_schema": schema
    }


def get_error_response(
    message: str,
    result: List[Any] = None,
    schema: Any = None
):
    return {
        "status": "error",
        "message": message,
        "result": [] if result is None else result,
        "_schema": schema
    }


def translate_schema(_, data: Any):
    if isinstance(data, str):
        return data

    for k, v in data.copy().items():
        if isinstance(v, dict):  # For DICT
            data[k] = translate_schema(_, v)
        elif isinstance(v, list):  # For LIST
            data[k] = [translate_schema(_, i) for i in v]
        elif isinstance(v, str) and k == "title":  # Update Key-Value
            data[k] = _(v)

    return data
