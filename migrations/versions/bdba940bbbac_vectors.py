"""vectors

Revision ID: bdba940bbbac
Revises: 
Create Date: 2025-02-18 10:09:18.336305

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text
from src.core.secrets import Config
from sqlalchemy.dialects.postgresql import UUID, JSON

# revision identifiers, used by Alembic.
revision: str = 'bdba940bbbac'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'document_vectors',
        sa.Column('id', UUID(as_uuid=True), server_default=text("gen_random_uuid()"), primary_key=True,
                  nullable=False),
        sa.Column('client_id', UUID(as_uuid=True), nullable=False),
        sa.Column('document_type', sa.String(length=100), nullable=True),
        sa.Column('document', sa.String, nullable=True),
        sa.Column('document_vector', sa.ARRAY(sa.Float()), nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP'),
                  onupdate=sa.text('CURRENT_TIMESTAMP')),
        schema=Config.SCHEMA_NAME
    )


def downgrade():
    op.drop_table('document_vectors', schema=Config.SCHEMA_NAME)
