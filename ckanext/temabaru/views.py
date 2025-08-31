from flask import Blueprint


temabaru = Blueprint(
    "temabaru", __name__)


def page():
    return "Hello, temabaru!"


temabaru.add_url_rule(
    "/temabaru/page", view_func=page)


def get_blueprints():
    return [temabaru]
