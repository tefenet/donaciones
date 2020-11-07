"""create shifts table

Revision ID: bb13f2d0ce00
Revises: 7ea45a8121d7
Create Date: 2020-11-03 01:39:59.114637

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey

revision = 'bb13f2d0ce00'
down_revision = '7ea45a8121d7'
branch_labels = None
depends_on = None


def upgrade():
    shifts_table = op.create_table(
        'shifts',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('donor_email', sa.String(60), nullable=False),
        sa.Column('donor_phone', sa.String(30)),
        sa.Column('start_time', sa.Time(), nullable=False),
        sa.Column('end_time', sa.Time(), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('center_id', sa.Integer, ForeignKey('centers.id')),
    )


def downgrade():
    op.drop_table('shifts')
