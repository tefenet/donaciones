"""create role table

Revision ID: ea0bf8964e49
Revises: 54e1f29b4573
Create Date: 2020-10-18 20:18:31.295562

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ea0bf8964e49'
down_revision = '54e1f29b4573'
branch_labels = None
depends_on = None

"""
class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    users = relationship('User', secondary=user_has_rol, backref='role')
"""


def upgrade():
    roles_table = op.create_table('roles',
                                  sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
                                  sa.Column('name', sa.String(100), nullable=False),
                                  )
    # seed de roles:

    op.bulk_insert(roles_table,
                   [
                       {
                           'id': 'Administrador', 'name': '',
                       },
                       {
                           'name': 'Operador del Centro de Ayuda',
                       }
                   ]
                   )


def downgrade():
    op.drop_table('roles')
