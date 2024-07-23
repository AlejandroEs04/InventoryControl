def get_action_products(data):
    processed_data = []
    
    for action in data: 
        for product in action['products']:
            processed_data.append({
                'action_id' : action['id'], 
                'date' : action['date'], 
                'item_id' : product['id'],
                'quantity' : product['quantity']
            })
    
    return processed_data