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