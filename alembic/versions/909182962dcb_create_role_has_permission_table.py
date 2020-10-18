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
    role_has_permission_table = op.create_table(
        'role_has_permission',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('role_id', sa.Integer, nullable=False),
        sa.Column('permission_id', sa.Integer, nullable=False),
    )

    op.bulk_insert(role_has_permission_table,
                   [
                       {'role_id': 1, 'permission_id': 1},  # user_index
                       {'role_id': 1, 'permission_id': 2},  # user_show
                       {'role_id': 1, 'permission_id': 3},  # user_destroy
                       {'role_id': 1, 'permission_id': 4},  # user_update
                       {'role_id': 1, 'permission_id': 5},  # user_find
                       {'role_id': 1, 'permission_id': 6},  # user_show
                       {'role_id': 1, 'permission_id': 7},  # role_index
                       {'role_id': 1, 'permission_id': 8},  # role_new
                       {'role_id': 1, 'permission_id': 9},  # role_show
                       {'role_id': 1, 'permission_id': 10},  # role_destroy
                       {'role_id': 1, 'permission_id': 11},  # role_update
                       {'role_id': 1, 'permission_id': 12},  # permission_index
                       {'role_id': 1, 'permission_id': 13},  # permission_show
                       {'role_id': 1, 'permission_id': 14},  # permission_new
                       {'role_id': 1, 'permission_id': 15},  # permission_destroy
                       {'role_id': 1, 'permission_id': 16},  # permission_update
                       {'role_id': 1, 'permission_id': 17},  # system_modify_config
                       {'role_id': 1, 'permission_id': 18},  # user_admin_login_logout
                   ])


def downgrade():
    op.drop_table('role_has_permission')
