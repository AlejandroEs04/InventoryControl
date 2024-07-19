from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.services.data_service import analyze_data

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/', methods=['POST'])
@swag_from('swagger_docs/analyze.yml')
def analyze():
    data = request.get_json()
    result = analyze_data(data)
    return jsonify(result)
