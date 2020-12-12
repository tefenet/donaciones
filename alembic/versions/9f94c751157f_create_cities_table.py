"""create_cities_table

Revision ID: 9f94c751157f
Revises: bb13f2d0ce00
Create Date: 2020-12-12 09:43:40.534050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f94c751157f'
down_revision = 'bb13f2d0ce00'
branch_labels = None
depends_on = None


def upgrade():

    city_table = op.create_table(
        'city',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(100), nullable=False),
    )

    op.bulk_insert(city_table, [
        {
           "name": "La Plata"
        },
        {
           "name": "Buenos Aires"
        },
        {
           "name": "Bahia Blanca"
        },
        {
           "name": "Quilmes"
        },
        {
           "name": "Tandil"
        },
        {
           "name": "Neuquen"
        },
        {
           "name": "Bengkulu"
        },
        {
           "name": "Duluth"
        },
        {
           "name": "Brescia"
        },
        {
           "name": "Daknam"
        },
        {
           "name": "Argyle"
        },
        {
           "name": "Bensheim"
        },
        {
           "name": "Santa Coloma de Gramenet"
        },
        {
           "name": "Killa Saifullah"
        },
        {
           "name": "Serralunga d'Alba"
        },
        {
           "name": "Puno"
        },
        {
           "name": "Hertsberge"
        },
        {
           "name": "Pictou"
        },
        {
           "name": "Neerharen"
        },
        {
           "name": "Talagante"
        },
        {
           "name": "Patna"
        },
        {
           "name": "Akron"
        },
        {
           "name": "Grande Prairie"
        },
        {
           "name": "Thunder Bay"
        },
        {
           "name": "Thirimont"
        },
        {
           "name": "Tavier"
        },
        {
           "name": "Hartlepool"
        },
        {
           "name": "Anápolis"
        },
        {
           "name": "Pulderbos"
        },
        {
           "name": "Robelmont"
        },
        {
           "name": "Desteldonk"
        },
        {
           "name": "Grand Falls"
        },
        {
           "name": "Harrisburg"
        },
        {
           "name": "Toledo"
        },
        {
           "name": "Alva"
        },
        {
           "name": "Independence"
        }
        ])



def downgrade():
    op.drop_table('city')
