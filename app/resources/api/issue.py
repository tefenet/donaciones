from flask import jsonify
from app.models.issue import Issue


def index():
    issues = Issue.query.all()
    issues = list(map(lambda i: i.serialize(), issues))
    return jsonify(issues=issues)
