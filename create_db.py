from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
base = declarative_base()
base.metadata.create_all(bind=engine)
