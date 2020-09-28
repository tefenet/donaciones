from flask import jsonify
from app.models.issue import Issue


def index():
    issues = Issue.query.all()

    return jsonify(issues=issues)
