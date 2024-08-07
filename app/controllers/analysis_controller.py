from flask import Blueprint, request, jsonify
from app.services.data_service import analyze_total_products, analyze_action_by_period
from app.utils.get_processed_data import get_action_products

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/total_products', methods=['POST'])
def total_sales_analyze():
    data = request.get_json()
    result = analyze_total_products(get_action_products(data))
    return jsonify(result)

@analysis_bp.route('/actions_period', methods=['POST'])
def sales_period_analyze():
    data = request.get_json()
    result = analyze_action_by_period(get_action_products(data))
    return jsonify(result)

@analysis_bp.route('/inventory_stock', methods=['POST'])
def inventory_stock_analyze():
    data = request.get_json();
    print(data)
    
    return jsonify({ "msg": "Saludos" })