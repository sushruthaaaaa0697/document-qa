import uuid
from datetime import datetime
from src.core.secrets import Config
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, text, VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DocumentVectorizer(Base):
    __tablename__ = 'document_vectors'
    __table_args__ = {'schema': Config.SCHEMA_NAME}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_id = Column(UUID(as_uuid=True), nullable=False)
    document_type = Column(VARCHAR, nullable=False)
    document = Column(VARCHAR, nullable=False)
    document_vector = Column(VARCHAR, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, server_default=text('CURRENT_TIMESTAMP'))
