def get_action_products(data):
    processed_data = []
    
    for action in data: 
        for item in action['products']:
            processed_data.append({
                'action_id' : action['id'], 
                'date' : action['date'], 
                'item_id' : item['id'],
                'quantity' : item['quantity']
            })
    
    return processed_data

def get_actions_information(data):
    processed_data = []
    
    for action in data: 
        processed_data.append({
            'action_id' : action['id'], 
            'user_id' : action['user_id'], 
            'amount' : action['amount'], 
            'date' : action['date'] 
        })
    
    return processed_data

def get_items_info(data):
    processed_data = []
    
    for item in data:
        processed_data.append({
            'item_id' : item['id']
        })
        
    return processed_data