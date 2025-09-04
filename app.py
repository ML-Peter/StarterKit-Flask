

from flask import Flask
from dotenv import load_dotenv
from config.flask_config import Config
from config.database import DB_URI

from models.user import db
from models.account import Account
from routes.main_routes import main_bp
from routes.auth_routes import auth_bp
from routes.account_routes import account_bp

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
db.init_app(app)


app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(account_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=Config.DEBUG, host="0.0.0.0", port=5002)