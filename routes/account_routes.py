from flask import Blueprint
from controllers.account import edit_logic, profile_logic

account_bp = Blueprint('account', __name__, url_prefix='/account')

@account_bp.route('/edit', methods=['GET', 'POST'])
def edit():
    return edit_logic()

@account_bp.route('/profile')
def profile():
    return profile_logic()

@account_bp.route('/delete', methods=['POST'])
def delete_account():
    from controllers.account import delete_account_logic
    return delete_account_logic()
