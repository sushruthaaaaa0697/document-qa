import psycopg2
from src.core.secrets import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .pg_model import DocumentVectorizer
import logging

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db = SessionLocal()


class PostgreSQLConnector:
    def __init__(self):
        logging.info("Initializing PostgreSQL connection.")
        self.conn = psycopg2.connect(
            dbname=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASS,
            host=Config.DB_HOST,
            port=Config.DB_PORT
        )
        logging.info("PostgreSQL connection established successfully.")

    def write_to_db(self, client_id, doc_type, doc, doc_vector):
        new_record = DocumentVectorizer(
            client_id=client_id,
            document_type=doc_type,
            document=doc,
            document_vector=doc_vector,
        )
        db.add(new_record)

        # Commit the transaction
        db.commit()
        logging.info("New record committed to database successfully.")
        db.close()
        logging.info("Written new record to database")
