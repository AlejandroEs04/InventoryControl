from app.services.items_data_service import items_analyze

def test_items_analyze():
    response = items_analyze(
        [
            {'action_id': 2, 'date': '2024-07-19T15:19:35.991Z', 'item_id': '2003723-6980', 'quantity': 5}, 
            {'action_id': 2, 'date': '2024-07-19T15:19:35.991Z', 'item_id': '2003723-6800', 'quantity': 3}, 
            {'action_id': 3, 'date': '2024-07-19T15:19:35.991Z', 'item_id': '2001004-6980', 'quantity': 10}, 
            {'action_id': 3, 'date': '2024-07-19T15:19:35.991Z', 'item_id': '4005009-7000', 'quantity': 5}, 
            {'action_id': 4, 'date': '2024-07-19T15:19:35.991Z', 'item_id': '2003723-6980', 'quantity': 6}, 
            {'action_id': 5, 'date': '2024-07-19T15:19:35.991Z', 'item_id': '2003723-6980', 'quantity': 6}, 
            {'action_id': 5, 'date': '2024-07-19T15:19:35.991Z', 'item_id': '2001004-6980', 'quantity': 10}, 
            {'action_id': 5, 'date': '2024-07-19T15:19:35.991Z', 'item_id': '4005009-7000', 'quantity': 5}
        ]
    )
    
    print(response)
    
    return

test_items_analyze()