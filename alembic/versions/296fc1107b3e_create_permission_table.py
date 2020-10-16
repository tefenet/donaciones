"""create permiso table

Revision ID: 296fc1107b3e
Revises: e032fdcefd33
Create Date: 2020-10-16 06:42:44.861762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '296fc1107b3e'
down_revision = 'e032fdcefd33'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'permission',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade():
    def downgrade():
    	op.drop_table('permission')
