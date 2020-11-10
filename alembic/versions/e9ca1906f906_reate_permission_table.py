"""reate permission table

Revision ID: e9ca1906f906
Revises: a307937125d3
Create Date: 2020-10-18 22:02:27.609344

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e9ca1906f906'
down_revision = 'a307937125d3'
branch_labels = None
depends_on = None


def upgrade():
    permissions_table = op.create_table('permissions',
                                        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
                                        sa.Column('name', sa.String(100), nullable=False),
                                        )
    # seed de roles:

    op.bulk_insert(permissions_table,
                   [
                       {'id': 1, 'name': 'user_index'},
                       {'id': 2, 'name': 'user_new'},
                       {'id': 3, 'name': 'user_destroy'},
                       {'id': 4, 'name': 'user_update'},
                       {'id': 5, 'name': 'user_find'},
                       {'id': 6, 'name': 'user_show'},
                       {'id': 7, 'name': 'role_index'},
                       {'id': 8, 'name': 'role_new'},
                       {'id': 9, 'name': 'role_show'},
                       {'id': 10, 'name': 'role_destroy'},
                       {'id': 11, 'name': 'role_update'},
                       {'id': 12, 'name': 'permission_index'},
                       {'id': 13, 'name': 'permission_show'},
                       {'id': 14, 'name': 'permission_new'},
                       {'id': 15, 'name': 'permission_destroy'},
                       {'id': 16, 'name': 'permission_update'},
                       {'id': 17, 'name': 'system_modify_config'},
                       {'id': 18, 'name': 'user_admin_login_logout'},
                       {'id': 19, 'name': 'centro_index'},
                       {'id': 20, 'name': 'centro_new'},
                       {'id': 21, 'name': 'centro_destroy'},
                       {'id': 22, 'name': 'centro_update'},
                       {'id': 23, 'name': 'centro_show'},
                       {'id': 24, 'name': 'shifts_index'},
                       {'id': 25, 'name': 'shifts_new'},
                       {'id': 26, 'name': 'shifts_destroy'},
                       {'id': 27, 'name': 'shifts_update'},
                       {'id': 28, 'name': 'shifts_show'},
                       {'id': 29, 'name': 'shifts_search'},
                   ]
                   )


def downgrade():
    op.drop_table("permissions")
