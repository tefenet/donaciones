"""create issues table

Revision ID: b1f473747b2b
Revises: ca9f929dd635
Create Date: 2020-10-30 02:47:27.761839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1f473747b2b'
down_revision = 'ca9f929dd635'
branch_labels = None
depends_on = None


def upgrade():
    issues_table = op.create_table(
	    'issues',
	    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
	    sa.Column('email', sa.String(30)),
	    sa.Column('description', sa.Text),
	    sa.Column('category_id', sa.Integer, nullable=False, index= True),
	    sa.Column('status_id', sa.Integer, nullable=False, index= True),
	)

    op.bulk_insert(issues_table,
               [
                   {
                       'id': 1,
                       'email': 'fede@mail.com',
                       'description': 'No puedo iniciar sesión correctamente',
                       'category_id': 1,
                       'status_id': 1,

                   },
                   {
                       'id': 2,
                       'email': 'jose@mail.com',
                       'description': 'El sistema de dice que hay un error',
                       'category_id': 1,
                       'status_id': 2,

                   },
                   {
                       'id': 4,
                       'email': 'maria@mail.com',
                       'description': 'No tengo acceso al sistema',
                       'category_id': 1,
                       'status_id': 1,

                   },
               ]
    )


def downgrade():
     op.drop_table('issues')