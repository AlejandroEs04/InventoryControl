from flask import Blueprint, request, jsonify
from app.utils.get_processed_data import get_action_products
from app.services.items_data_service import items_analyze, major_minor_items_analyze, items_analyze_by_period

items_analysis_bp = Blueprint('product', __name__)

@items_analysis_bp.route('/', methods=['POST'])
def items_analysis():
    data = request.get_json()
    action_product_info = get_action_products(data)
    
    summatory_analysis, plot_image = items_analyze(action_product_info)
    summatory_analysis_by_period,_ = items_analyze_by_period(action_product_info)
    major_minor_analyzis = major_minor_items_analyze(summatory_analysis_by_period)
    
    summary = {"summary" : { "items_analyze" : summatory_analysis, "items_analyze_by_period" : summatory_analysis_by_period, "items_movements" : major_minor_analyzis, "plot_img" : plot_image }}
    
    return jsonify(summary)

