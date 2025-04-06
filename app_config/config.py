from flask import Flask
from .db import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:S1mpl3Bus1n3ss!@database:5432/crypto_wallet'
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    return app