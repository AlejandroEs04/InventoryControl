from flask import Blueprint, request, jsonify
from app.services.data_service import analyze_data

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/', methods=['POST'])
def analyze():
    data = request.get_json()
    result = analyze_data(data)
    return jsonify(result)
