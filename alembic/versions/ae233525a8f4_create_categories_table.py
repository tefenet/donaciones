"""create categories table

Revision ID: ae233525a8f4
Revises: b1f473747b2b
Create Date: 2020-10-30 07:48:20.829650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae233525a8f4'
down_revision = 'b1f473747b2b'
branch_labels = None
depends_on = None


def upgrade():
    categories_table = op.create_table(
	    'categories',
	    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
	    sa.Column('name', sa.String(50))
	)

    op.bulk_insert(categories_table,
               [
                   {
                       'id': 1,
                       'name': 'Bug',
                   },
                   {
                       'id': 2,
                       'name': 'Question',
                   },
               ]
    )


def downgrade():
	#eliminar foreign key contraint
    op.drop_table('categories')