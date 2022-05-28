def remove_nulls_from_dict(d: dict):
    result = {}
    for k, v in d.items():
        if v is not None:
            result[k] = v

    return result
