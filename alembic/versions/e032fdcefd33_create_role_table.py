"""create rol table

Revision ID: e032fdcefd33
Revises: 9b7544dca7ea
Create Date: 2020-10-16 06:30:32.491973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e032fdcefd33'
down_revision = '9b7544dca7ea'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'role',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade():
    def downgrade():
    	op.drop_table('role')
