from flask import Blueprint
from controllers.main import index_logic, accueil_logic

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    return index_logic()

@main_bp.route("/accueil")
def accueil():
    return accueil_logic()
