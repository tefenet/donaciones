"""add updated_time column

Revision ID: 9b7544dca7ea
Revises: 8f43b2ceeda9
Create Date: 2020-10-16 00:55:10.937918

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '9b7544dca7ea'
down_revision = '8f43b2ceeda9'
branch_labels = None
depends_on = None


def upgrade():
    """
        update_date = Column(DateTime, default=datetime.now())
    """
    op.add_column('users', sa.Column('update_date', sa.DateTime, default=None))


def downgrade():
    op.drop_column('users', 'update_date')
