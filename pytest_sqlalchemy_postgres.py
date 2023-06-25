from __future__ import annotations

from typing import TYPE_CHECKING

import sqlalchemy as sa
import pytest

if TYPE_CHECKING:
    from sqlalchemy import Engine, MetaData
    from sqlalchemy.orm import scoped_session


# --------------------------------------------------------------------------------


def setup_db_factory(engine: Engine, metadata: MetaData):
    @pytest.fixture(scope="session", autouse=True)
    def setup_db():
        """Create a `setup_db` fixture that manages the tables, sequences, &c."""
        # Drop all objects
        metadata.drop_all(bind=engine)

        # Create all objects
        metadata.create_all(bind=engine)

        # Run all tests
        yield

        # XXX: Drop followed by create is intentional. This allows the
        # developer to inspect the database after a failed test.

    return setup_db


def db_factory(engine: Engine, Session: scoped_session):
    """Create a `db` fixture that manages a per-test transaction and SQLAlchemy session.
    Ref: https://docs.sqlalchemy.org/en/20/orm/session_transaction.html#joining-a-session-into-an-external-transaction-such-as-for-test-suites
    """

    @pytest.fixture
    def db(setup_db):
        """Manages a per-test transaction with a bound session."""
        # Setup a session bound to a nested transaction
        conn = engine.connect()
        transaction = conn.begin()
        session = Session(bind=conn)
        session.begin_nested()

        # This ensures that every call to `session.commit()` creates a new savepoint.
        # We're basically replacing BEGIN ... COMMIT with SAVEPOINT ... RELEASE SAVEPOINT
        # inside our nested transaction.
        # In SQLAlchemy 2.0 this is handled by the `join_transaction_mode` kwarg to `Session`
        # Ref: https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session.params.join_transaction_mode
        @sa.event.listens_for(session, "after_transaction_end")
        def restart_savepoint(_, transaction):
            if transaction.nested and not transaction._parent.nested:
                # ... then this is the topmost nested transaction
                # (i.e: the one we created above)
                session.expire_all()
                session.begin_nested()

        # Run the test
        yield session

        # Rollback the last savepoint + outer transaction
        Session.remove()
        transaction.rollback()
        conn.close()

    return db
