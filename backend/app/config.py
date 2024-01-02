from typing import List
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

###
# Properties configurations
###

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Authorization"

config = Config(".env")

ROUTE_PREFIX_V1 = "/v1"

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)


DATABASE_URL = 'postgresql://postgres:123456@localhost:5432/fitness_challenge_db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
