import pytest
import sqlalchemy as sa
from helpers import User


@pytest.mark.parametrize("n", range(100))
def test_ok(db, n):
    user = User()
    db.add(user)
    db.commit()
    assert len(db.query(User).all()) == 1


def test_error(db):
    with pytest.raises(
        sa.exc.InvalidRequestError,
        match="A transaction is already begun on this Session.",
    ):
        db.begin()
