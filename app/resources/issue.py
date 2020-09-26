from flask import redirect, render_template, request, url_for
from app.db import dbSession
from app.models.issue import Issue


# Public resources
def index():
    # issues = dbSession.query(Issue).all()
    issues = Issue.query.all()
    return render_template("issue/index.html", issues=issues)


def new():
    return render_template("issue/new.html")


def create():
    args = list(request.form.values())
    issue = Issue(email=args[0], description=args[1], category_id=args[2], status_id=args[3])
    dbSession.add(issue)
    dbSession.commit()
    return redirect(url_for("issue_index"))
