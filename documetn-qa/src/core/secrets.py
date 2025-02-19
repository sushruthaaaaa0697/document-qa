"""POSTGRESQL CONNECTIONS"""


class Config:
    SCHEMA_NAME = "vectors"
    DB_NAME = "postgres"
    DB_USER = "postgres"
    DB_PASS = "master123"
    DB_HOST = "localhost"
    DB_PORT = 5433
    SQLALCHEMY_DATABASE_URI = f"""postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"""
