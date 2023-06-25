from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine("postgresql://localhost/foo")

Base = declarative_base()


class User(Base):
    __tablename__ = "test_user"
    id = Column(Integer(), primary_key=True)


metadata = Base.metadata

Session = scoped_session(sessionmaker(bind=engine))
