from sqlalchemy import func
from sqlalchemy.orm.query import Query


def get_count(q: Query):
    """
    Return the number of rows that matches a query
    """
    count_q = q.statement.with_only_columns(func.count(),
                                            maintain_column_froms=True).order_by(
        None)
    count = q.session.execute(count_q).scalar()
    return count
