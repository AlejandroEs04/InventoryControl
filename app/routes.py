from flask import Flask
from app.controllers.analysis_controller import analysis_bp

def create_app():
    app = Flask(__name__)
    
    # Here will be every routes
    app.register_blueprint(analysis_bp, url_prefix='/analysis')
    
    return app