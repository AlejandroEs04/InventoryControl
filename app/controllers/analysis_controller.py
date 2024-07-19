from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.services.data_service import analyze_data

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/', methods=['POST'])
@swag_from('swagger_docs/analyze.yml')
def analyze():
    data = request.get_json()
    
    processed_data = []
    
    for sale in data: 
        for product in sale['products']:
            processed_data.append({
                'sale_id' : sale['id'], 
                'date' : sale['date'], 
                'product_id' : product['id'],
                'quantity' : product['quantity']
            })
    
    result = analyze_data(processed_data)
    return jsonify(result)
