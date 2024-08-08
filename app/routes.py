from flask import Flask
from flasgger import Swagger
from app.controllers.items_analysis_controller import items_analysis_bp
from app.controllers.actions_analysis_controller import actions_analysis_bp

def create_app():
    app = Flask(__name__)
    Swagger(app)
    
    app.register_blueprint(items_analysis_bp, url_prefix='/api/product-analysis')
    app.register_blueprint(actions_analysis_bp, url_prefix='/api/action-analysis')
    
    return app