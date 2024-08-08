from flask import Blueprint, request, jsonify
from app.utils.get_processed_data import get_actions_information
from app.services.actions_data_service import actions_analyse

actions_analysis_bp = Blueprint('action', __name__)

@actions_analysis_bp.route('/', methods=['POST'])
def actions_analysis():
    data = request.get_json()    
    actions_total, amount_total = actions_analyse(get_actions_information(data))
    
    summary = { 'actions_total' : actions_total, 'amount_total' : amount_total }
    return jsonify(summary)