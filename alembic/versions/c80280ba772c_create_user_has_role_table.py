"""create user has role table

Revision ID: c80280ba772c
Revises: 909182962dcb
Create Date: 2020-10-16 07:11:30.591623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c80280ba772c'
down_revision = '909182962dcb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_has_role',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('role_id', sa.Integer, nullable=False),
    )


def downgrade():
   	op.drop_table('user_has_role')
