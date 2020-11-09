"""create shifts table

Revision ID: bb13f2d0ce00
Revises: 7ea45a8121d7
Create Date: 2020-11-03 01:39:59.114637

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey

from datetime import time, datetime, date, timedelta

revision = 'bb13f2d0ce00'
down_revision = '7ea45a8121d7'
branch_labels = None
depends_on = None


def increment_time(t):
    t1 = datetime.strptime(str(t), '%H:%M:%S')
    t2 = datetime.strptime(str(time(0, 30)), '%H:%M:%S')
    time_zero = datetime.strptime(str(time(0)), '%H:%M:%S')
    return (t1 - time_zero + t2).time()


def increment_datetime(d):
    return (d + timedelta(2))


def upgrade():
    shifts_table = op.create_table(
        'shifts',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('donor_email', sa.String(60), nullable=False),
        sa.Column('donor_phone', sa.String(30)),
        sa.Column('start_time', sa.Time(), nullable=False),
        sa.Column('end_time', sa.Time(), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('center_id', sa.Integer, ForeignKey('centers.id')),
    )

    turnos = []
    hora_inicio = time(9, 00)
    hora_fin = time(9, 30)
    for i in range(1, 15):
        turno = {
            'id': i, 'donor_email': 'donor{}@test.com'.format(i), 'donor_phone': '+54 555 555-5555',
            'start_time': hora_inicio, 'end_time': hora_fin, 'date': '2020-11-07', 'center_id': 1
        }
        hora_inicio = increment_time(hora_inicio)
        hora_fin = increment_time(hora_fin)
        turnos.append(turno)
    op.bulk_insert(shifts_table, turnos)

    turnos = []
    hora_inicio = time(11, 00)
    hora_fin = time(11, 30)
    for i in range(15, 21):
        turno = {
            'id': i, 'donor_email': 'donor{}@test.com'.format(i), 'donor_phone': '+54 555 555-5555',
            'start_time': hora_inicio, 'end_time': hora_fin, 'date': '2020-11-06', 'center_id': 2
        }
        hora_inicio = increment_time(hora_inicio)
        hora_fin = increment_time(hora_fin)
        turnos.append(turno)
    op.bulk_insert(shifts_table, turnos)

    turnos = []
    hora_inicio = time(9, 30)
    hora_fin = time(10, 00)
    for i in range(21, 32):
        center_id = 2 if i <= 26 else 3 if i > 26 else 1
        turno = {
            'id': i, 'donor_email': 'donor{}@test.com'.format(i), 'donor_phone': '+54 555 555-5555',
            'start_time': hora_inicio, 'end_time': hora_fin, 'date': date.today(), 'center_id': center_id
        }
        hora_inicio = increment_time(hora_inicio)
        hora_fin = increment_time(hora_fin)
        turnos.append(turno)

    op.bulk_insert(shifts_table, turnos)

    # muchos turnos para un mismo correo
    turnos = []
    hora_inicio = time(9, 30)
    hora_fin = time(10, 00)
    dia = datetime.now()
    for i in range(32, 45):
        center_id = 4 if i <= 38 else 1 if i > 38 else 1
        turno = {
            'id': i, 'donor_email': 'donor77@test.com'.format(i), 'donor_phone': '+54 555 555-5555',
            'start_time': hora_inicio, 'end_time': hora_fin, 'date': dia.date(), 'center_id': center_id
        }
        hora_inicio = increment_time(hora_inicio)
        hora_fin = increment_time(hora_fin)
        if i == 37:
            dia = increment_datetime(dia)
        turnos.append(turno)

    op.bulk_insert(shifts_table, turnos)


def downgrade():
    op.drop_table('shifts')
