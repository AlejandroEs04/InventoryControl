from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.services.data_service import analyze_total_products, analyze_action_by_period

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/total_sales', methods=['POST'])
@swag_from('swagger_docs/analyze.yml')
def total_sales_analyze():
    # Total products sales
    data = request.get_json()
    
    processed_data = []
    
    for sale in data: 
        for product in sale['products']:
            processed_data.append({
                'action_id' : sale['id'], 
                'date' : sale['date'], 
                'item_id' : product['id'],
                'quantity' : product['quantity']
            })
    
    result = analyze_total_products(processed_data)
    return jsonify(result)

@analysis_bp.route('/sales_period', methods=['POST'])
@swag_from('swagger_docs/analyze.yml')
def sales_period_analyze():
    # Total products sales
    data = request.get_json()
    
    processed_data = []
    
    for sale in data: 
        for product in sale['products']:
            processed_data.append({
                'action_id' : sale['id'], 
                'date' : sale['date'], 
                'item_id' : product['id'],
                'quantity' : product['quantity']
            })
    
    result = analyze_action_by_period(processed_data)
    return jsonify(result)
