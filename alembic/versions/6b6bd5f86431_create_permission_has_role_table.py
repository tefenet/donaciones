"""create permission_has_role table

Revision ID: 6b6bd5f86431
Revises: e9ca1906f906
Create Date: 2020-10-18 22:09:25.770120

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6b6bd5f86431'
down_revision = 'e9ca1906f906'
branch_labels = None
depends_on = None


def upgrade():
    role_has_permission = op.create_table('role_has_permission',
                                          sa.Column('permissions_id', sa.Integer, primary_key=True),
                                          sa.Column('roles_id', sa.Integer, primary_key=True),
                                          )

    """Role 1 Admin
    Role 2 Operador"""

    op.bulk_insert(role_has_permission,
                   [
                       {
                           'roles_id': 1,
                           'permissions_id': 1,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 2,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 3,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 4,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 5,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 6,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 7,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 8,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 9,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 10,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 11,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 12,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 13,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 14,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 15,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 16,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 17,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 18,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 19,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 20,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 21,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 22,
                       },
                       {
                           'roles_id': 1,
                           'permissions_id': 23,
                       },
                       {
                           'roles_id': 2,
                           'permissions_id': 19,
                       },
                       {
                           'roles_id': 2,
                           'permissions_id': 20,
                       },
                       {
                           'roles_id': 2,
                           'permissions_id': 21,
                       },
                       {
                           'roles_id': 2,
                           'permissions_id': 22,
                       },
                       {
                           'roles_id': 2,
                           'permissions_id': 23,
                       },
                   ]
                   )


def downgrade():
    op.drop_table('role_has_permission')
