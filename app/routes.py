from flask import Flask
from flasgger import Swagger
from app.controllers.analysis_controller import analysis_bp

def create_app():
    app = Flask(__name__)
    Swagger(app)
    
    # Here will be every routes
    app.register_blueprint(analysis_bp, url_prefix='/api/analysis')
    
    return app