import pytest
from sqlalchemy import text

from .db_configs import DBConfig
from .db_connection import DBConnectionHandler


@pytest.mark.skip(reason="Sensitive test.")
def test_get_engine():
    db_conn = DBConnectionHandler()
    engine = db_conn.get_engine()

    assert engine is not None
    assert str(engine.url) == DBConfig.CONN_STRING
