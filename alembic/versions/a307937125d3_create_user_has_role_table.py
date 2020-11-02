"""create user_has_role table

Revision ID: a307937125d3
Revises: ea0bf8964e49
Create Date: 2020-10-18 20:46:18.888699

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a307937125d3'
down_revision = 'ea0bf8964e49'
branch_labels = None
depends_on = None

"""
user_has_role = Table('user_has_role', Base.metadata,
                      Column('roles_id', Integer, ForeignKey('roles.id')),
                      Column('users_id', Integer, ForeignKey('users.id'))
                      )

"""


def upgrade():
    user_has_role = op.create_table('user_has_role',
                                    sa.Column('roles_id', sa.Integer, primary_key=True),
                                    sa.Column('users_id', sa.Integer, primary_key=True),
                                    )

    """Role 1 Admin
    Role 2 Operador"""

    op.bulk_insert(user_has_role,
                   [
                       {
                           'roles_id': 1,
                           'users_id': 1,
                       },
                       {
                           'roles_id': 1,
                           'users_id': 2,
                       },
                       {
                           'roles_id': 2,
                           'users_id': 1,
                       },
                       {
                           'roles_id': 2,
                           'users_id': 3,
                       },
                       {
                           'roles_id': 2, 'users_id': 4,
                       },
                       {
                           'roles_id': 2, 'users_id': 5,
                       },
                       {
                           'roles_id': 2, 'users_id': 6,
                       },
                       {
                           'roles_id': 2, 'users_id': 7,
                       },
                       {
                           'roles_id': 2, 'users_id': 8,
                       },
                       {
                           'roles_id': 2, 'users_id': 9,
                       },
                       {
                           'roles_id': 2, 'users_id': 10,
                       },
                       {
                           'roles_id': 2, 'users_id': 11,
                       },
                       {
                           'roles_id': 2, 'users_id': 12,
                       },
                       {
                           'roles_id': 2, 'users_id': 13,
                       },
                       {
                           'roles_id': 2, 'users_id': 14,
                       },
                       {
                           'roles_id': 2, 'users_id': 15,
                       },
                       {
                           'roles_id': 2, 'users_id': 16,
                       },
                       {
                           'roles_id': 2, 'users_id': 17,
                       },
                       {
                           'roles_id': 2, 'users_id': 18,
                       },
                   ]
                   )


def downgrade():
    op.drop_table('user_has_role')
