from flask import jsonify
from app.db import dbSession
from app.models.issue import Issue


def index():
    issues = dbSession.query(Issue).all()

    return jsonify(issues=issues)
