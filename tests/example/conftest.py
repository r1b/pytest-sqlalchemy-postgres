from pytest_sqlalchemy_postgres import db_factory, setup_db_factory

from helpers import engine, metadata, Session


setup_db = setup_db_factory(engine, metadata)
db = db_factory(engine, Session)
