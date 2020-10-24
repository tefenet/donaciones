"""create users table v2

Revision ID: 8f43b2ceeda9
Revises:
Create Date: 2020-10-15 21:52:35.127734

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '8f43b2ceeda9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    active = Column(Boolean)
    account_type = Column(SmallInteger)
    create_date = Column(DateTime, default=datetime.now())"""

    users_table = op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(100), nullable=False, unique=True, index=True),
        sa.Column('username', sa.String(100), nullable=False, unique=True, index=True),
        sa.Column('password_hash', sa.String(100), nullable=True),
        sa.Column('first_name', sa.String(100)),
        sa.Column('last_name', sa.String(100)),
        sa.Column('active', sa.Boolean(), default=False, index=True),
        sa.Column('account_type', sa.SmallInteger(), default=2),
        sa.Column('create_date', sa.DateTime, default=datetime.now())
    )

    # seed de usuarios de prueba:

    op.bulk_insert(users_table,
                   [
                       {
                           'username': 'admin',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Admin',
                           'last_name': 'Admin',
                           'email': 'admin@donaciones.gov',
                           'active': True,
                           'account_type': 1,
                       },
                       {
                           'username': 'creepy29',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'John',
                           'last_name': 'Doe',
                           'email': 'john@donaciones.gov',
                           'active': True,
                           'account_type': 1,
                       },
                       {
                           'username': 'ediaz',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Emiliano',
                           'last_name': 'Diaz',
                           'email': 'ediaz@donaciones.gov',
                           'active': False,
                           'account_type': 2,
                       },
                       {
                           'username': 'ramond',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Ramon',
                           'last_name': 'Diaz',
                           'email': 'ramond@donaciones.gov',
                           'active': True,
                           'account_type': 2,
                       },
                       {
                           'username': 'jsv11',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Juan Sebastian',
                           'last_name': 'Veron',
                           'email': 'jsv11@donaciones.gov',
                           'active': True,
                           'account_type': 2,
                       },
                       {
                           'username': 'petertroglio',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Peter',
                           'last_name': 'Troglio',
                           'email': 'petertroglio@donaciones.gov',
                           'active': False,
                           'account_type': 2,
                       },
                       {
                           'username': 'nassuti_c',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Cristian',
                           'last_name': 'Nassuti',
                           'email': 'cnassuti@donaciones.gov',
                           'active': False,
                           'account_type': 2,
                       },
                       {
                           'username': 'diego',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Diego',
                           'last_name': 'Marado',
                           'email': 'dieguito@donaciones.gov',
                           'active': True,
                           'account_type': 2,
                       },
                       {
                           'username': 'pepechatruc',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'José',
                           'last_name': 'Chatruc',
                           'email': 'pepechatruc@donaciones.gov',
                           'active': False,
                           'account_type': 2,
                       },
                       {
                           'username': 'diSefano',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Alfredo',
                           'last_name': 'Di Stefano',
                           'email': 'alfredo@donaciones.gov',
                           'active': True,
                           'account_type': 2,
                       },
                       {
                           'username': 'toni23',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Toni',
                           'last_name': 'Capone',
                           'email': 'tonicapone@donaciones.gov',
                           'active': False,
                           'account_type': 2,
                       },
                       {
                           'username': 'brunodiaz',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Bruno',
                           'last_name': 'Diaz',
                           'email': 'bdiaz@donaciones.gov',
                           'active': True,
                           'account_type': 2,
                       },
                       {
                           'username': 'ramonete',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Ramon',
                           'last_name': 'Ayala',
                           'email': 'pepeayala@donaciones.gov',
                           'active': True,
                           'account_type': 2,
                       },
                       {
                           'username': 'pepe',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Pepe',
                           'last_name': 'Diaz',
                           'email': 'd.pepe@donaciones.gov',
                           'active': True,
                           'account_type': 2,
                       },
                       {
                           'username': 'usuario',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'default',
                           'last_name': 'user',
                           'email': 'default@donaciones.gov',
                           'active': True,
                           'account_type': 2,
                       },
                       {
                           'username': 'testing',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'test',
                           'last_name': 'test',
                           'email': 'test@donaciones.gov',
                           'active': False,
                           'account_type': 2,
                       },
                       {
                           'username': 'juan',
                           'password_hash': 'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579',
                           'first_name': 'Juan',
                           'last_name': 'Lopez',
                           'email': 'juan@donaciones.gov',
                           'active': True,
                           'account_type': 2,
                       },
                   ]
                   )


def downgrade():
    op.drop_table('users')
