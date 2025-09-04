from flask import Blueprint
from controllers.auth import login_logic, register_logic, logout_logic

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return login_logic()

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return register_logic()

@auth_bp.route('/logout')
def logout():
    return logout_logic()
