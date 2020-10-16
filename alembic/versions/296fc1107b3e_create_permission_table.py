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
    permission_table = op.create_table(
        'permission',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )

    op.bulk_insert(permission_table,
    [
        {'id':1, 'name':'user_index'},
        {'id':2, 'name':'user_new'},
        {'id':3, 'name':'user_destroy'},
        {'id':4, 'name':'user_update'},
        {'id':5, 'name':'user_find'},
        {'id':6, 'name':'user_show'},
        {'id':7, 'name':'role_index'},
        {'id':8, 'name':'role_new'},
        {'id':9, 'name':'role_show'},
        {'id':10, 'name':'role_destroy'},
        {'id':11, 'name':'role_update'},
        {'id':12, 'name':'permission_index'},
        {'id':13, 'name':'permission_show'},
        {'id':14, 'name':'permission_new'},
        {'id':15, 'name':'permission_destroy'},
        {'id':16, 'name':'permission_update'},
        {'id':17, 'name':'system_modify_config'},
        {'id':18, 'name':'user_admin_login_logout'},
    ]
 )

def downgrade():
    op.drop_table('permission')
