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
    user_has_role_table = op.create_table(
        'user_has_role',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('role_id', sa.Integer, nullable=False),
    )

    op.bulk_insert(user_has_role_table,
                   [
                       {'id': 1, 'user_id': 1, 'role_id': 1},
                       {'id': 2, 'user_id': 2, 'role_id': 2},
                   ]
                   )


def downgrade():
    op.drop_table('user_has_role')
