"""create statuses table

Revision ID: 7ea45a8121d7
Revises: ae233525a8f4
Create Date: 2020-10-30 07:48:31.087401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ea45a8121d7'
down_revision = 'ae233525a8f4'
branch_labels = None
depends_on = None


def upgrade():
    statuses_table = op.create_table(
	    'statuses',
	    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
	    sa.Column('name', sa.String(30))
	)

    op.bulk_insert(statuses_table,
               [
                   {
                       'id': 1,
                       'name': 'New',
                   },
                   {
                       'id': 2,
                       'name': 'Todo',
                   },
                   {
                       'id': 3,
                       'name': 'In progress',
                   },
               ]
    )


def downgrade():
	#eliminar foreign key contraint
    op.drop_table('statuses')