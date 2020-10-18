"""create users table v2

Revision ID: 8f43b2ceeda9
Revises: 2f60ede5f8b6
Create Date: 2020-10-15 21:52:35.127734

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '8f43b2ceeda9'
down_revision = '2f60ede5f8b6'
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
        sa.Column('first_name', sa.String(100), index=True),
        sa.Column('last_name', sa.String(100), index=True),
        sa.Column('active', sa.Boolean(), default=False, index=True),
        sa.Column('account_type', sa.SmallInteger(), default=2),
        sa.Column('create_date', sa.DateTime, default=datetime.now())
    )

    #seed de usuarios de prueba:

    op.bulk_insert(users_table,
    [
        {'id':1, 'username':'admin', 'password_hash':'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579', 
        'first_name':'Admin', 'last_name':'Del Sitio', 'email':'admin@donaciones.gov', 'active':True, 'account_type': 1, 'create_date': '2020-10-16 01:03:03'},
        {'id':2, 'username':'operador', 'password_hash':'pbkdf2:sha256:150000$QhWXVmaA$2028ef705c136b76d37f8e306cb8f4fab11fc63a58a8dd7ed6ea150a385a4579', 
        'first_name':'Operador', 'last_name':'Del Centro', 'email':'operadorUNICEF@gmail.com', 'active':True, 'account_type': 2, 'create_date': '2020-10-16 01:03:03'},
    ]
)



def downgrade():
    op.drop_table('users')
