from flask import jsonify
from app.models.shifts import Shifts


def index():
    # falta paginar y autenticar

    shifts = Shifts.all()
    shifts = list(map(lambda i: i.serialize(), shifts))
    return jsonify(shifts=shifts)
