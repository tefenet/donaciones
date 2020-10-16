"""create users table v2

Revision ID: 8f43b2ceeda9
Revises: 2f60ede5f8b6
Create Date: 2020-10-15 21:52:35.127734

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '8f43b2ceeda9'
down_revision = '2f60ede5f8b6'
branch_labels = None
depends_on = None


def upgrade():
    """
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    active = Column(Boolean)
    account_type = Column(SmallInteger)
    create_date = Column(DateTime, default=datetime.now())"""

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(100), nullable=False, unique=True, index=True),
        sa.Column('username', sa.String(100), nullable=False, unique=True, index=True),
        sa.Column('password_hash', sa.String(100), nullable=True),
        sa.Column('first_name', sa.String(100), index=True),
        sa.Column('last_name', sa.String(100), index=True),
        sa.Column('active', sa.Boolean(), default=False, index=True),
        sa.Column('account_type', sa.SmallInteger(), default=2),
        sa.Column('create_date', sa.DateTime, default=datetime.now())
    )


def downgrade():
    op.drop_table('users')
