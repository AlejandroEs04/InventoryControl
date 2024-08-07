from flask import Blueprint, request, jsonify
from app.utils.get_processed_data import get_action_products
from app.services.items_data_service import items_analyze, major_minor_items_analyze

items_analysis_bp = Blueprint('product', __name__)

@items_analysis_bp.route('/', methods=['POST'])
def items_analysis():
    data = request.get_json()
    summatory_analysis = items_analyze(get_action_products(data))
    major_minor_analyzis = major_minor_items_analyze(summatory_analysis)
    
    summary = {"summary" : { "items_analyze" : summatory_analysis, "items_movements" : major_minor_analyzis }}
    
    return jsonify(summary)

