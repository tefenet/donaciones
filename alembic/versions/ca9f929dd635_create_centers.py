"""create centers

Revision ID: ca9f929dd635
Revises: 6b6bd5f86431
Create Date: 2020-10-22 19:20:54.757635

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey

revision = 'ca9f929dd635'
down_revision = '6b6bd5f86431'
branch_labels = None
depends_on = None


def upgrade():
    city_table = op.create_table(
        'city',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('description', sa.String(100), nullable=False),
    )
    type_table = op.create_table(
        'centerType',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('description', sa.String(100), nullable=False),
    )
    centers_table = op.create_table(
        'centers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(100), nullable=False, unique=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('address', sa.String(100), nullable=True),
        sa.Column('phone', sa.String(100)),
        sa.Column('web_site', sa.String(100)),
        sa.Column('published', sa.Boolean(), default=False),
        sa.Column('geo_location', sa.String(100)),
        sa.Column('opening', sa.DateTime, default=datetime.now()),
        sa.Column('closing', sa.DateTime, default=datetime.now()),
        sa.Column('protocol', sa.LargeBinary()),
        sa.Column('city_id', sa.Integer, ForeignKey('city.id')),
        sa.Column('type_id', sa.Integer, ForeignKey('centerType.id')),
    )

    op.bulk_insert(city_table,
                   [
                       {
                           'description': 'mendoza',
                       },
                       {
                           'description': 'bulonge',
                       },
                       {
                           'description': 'avellaneda',
                       },
                       {
                           'description': 'la plata',
                       },
                       {
                           'description': 'retiro',
                       },
                       {
                           'description': 'caseros',
                       }
                   ])
    op.bulk_insert(type_table,
                   [
                       {
                           'description': 'ropa',
                       },
                       {
                           'description': 'comida',
                       }

                   ])
    op.bulk_insert(
                   centers_table,
                   [
                       {
                           'name': 'one',
                           'address': 'eee',
                           'phone': '986986',
                           'email': 'holo@mail.com',
                           'web_site': 'qoinon',
                           'city_id': 1,
                           'type_id': 2,
                       },
                       {
                           'name': 'two',
                           'address': 'eee',
                           'phone': '986986',
                           'email': 'howwwlo@mail.com',
                           'web_site': 'qoinon',
                           'city_id': 2,
                           'type_id': 1,
                       },
                       {
                           'name': 'avellanedaAyuda',
                           'address': 'gral gallardo 123',
                           'phone': '986986',
                           'email': 'ayudavellaneda@mail.com',
                           'web_site': 'ayuda.com',
                           'city_id': 3,
                           'type_id': 1,
                       }
                   ]
                   )


def downgrade():
    op.drop_table('centerType')
    op.drop_table('city')
    op.drop_table('type')
