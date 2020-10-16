"""create role has permission table

Revision ID: 909182962dcb
Revises: 296fc1107b3e
Create Date: 2020-10-16 07:11:09.293161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '909182962dcb'
down_revision = '296fc1107b3e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'role_has_permission',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('role_id', sa.Integer, nullable=False),
        sa.Column('permission_id', sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table('role_has_permission')
