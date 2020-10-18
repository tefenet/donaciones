"""create system table

Revision ID: ec5b784bec0d
Revises: c80280ba772c
Create Date: 2020-10-17 21:13:37.929102

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'ec5b784bec0d'
down_revision = 'c80280ba772c'
branch_labels = None
depends_on = None


def upgrade():
    """
    __tablename__ = 'sistema'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(50))
    descripcion = Column(String)
    bienvenida = Column(String)
    email = Column(String(25))
    cant_por_pagina = Column(Integer, nullable=False)
    update_date = Column(DateTime)
    habilitado = Column(Boolean, default=True)
    """

    users_table = op.create_table(
        'sistema',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('titulo', sa.String(100), nullable=False),
        sa.Column('descripcion', sa.Text(65535), nullable=True),
        sa.Column('bienvenida', sa.Text(65535), nullable=True),
        sa.Column('email', sa.String(100), nullable=True),
        sa.Column('cant_por_pagina', sa.SmallInteger(), nullable=False, default=25),
        sa.Column('habilitado', sa.Boolean(), default=False),
        sa.Column('update_date', sa.DateTime(), nullable=True)
    )

    # seed de usuarios de prueba:

    op.bulk_insert(users_table,
                   [
                       {
                           'titulo': 'Centros de Ayuda BA',
                           'descripcion': 'Descripcion del sitio',
                           'bienvenida': 'Bienvenido a la pagina de administración de Centros de Ayuda BA',
                           'email': 'admin@donaciones.gov',
                           'cant_por_pagina': '5',
                           'habilitado': True
                       }
                   ]
                   )


def downgrade():
    op.drop_table('sistema')
