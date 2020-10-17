"""create system config table

Revision ID: ad9368bdf96b
Revises: c80280ba772c
Create Date: 2020-10-17 05:33:21.580736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad9368bdf96b'
down_revision = 'c80280ba772c'
branch_labels = None
depends_on = None


def upgrade():
    
    system_config_table = op.create_table(
        'system_config',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('value', sa.String(100), nullable=False),
    )

    op.bulk_insert(system_config_table,
    [
    	{'id': 1, 'name':'sitio_habilitado', 'value':'1'},
        {'id': 2, 'name':'titulo', 'value':'Donaciones.gov'},
        {'id': 3, 'name':'bienvenida', 'value':'Bienvenido a nuestro sitio'},
        {'id': 4, 'name':'email', 'value':'contacto@donaciones.gov'},
        {'id': 5, 'name':'descripcion', 'value':'Sitio para facilitar la realizacion de donaciones en el contexto de pandemia por COVID19'},
        {'id': 6, 'name':'cant_por_pagina', 'value':9},
    ]
)

def downgrade():
    op.drop_table('system_config')


        