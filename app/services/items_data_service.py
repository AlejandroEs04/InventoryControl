import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import io 
import base64

def items_analyze(data):
    df = pd.DataFrame(data)
    summary = df.groupby('item_id')['quantity'].sum().reset_index().to_dict('records')
    
    return summary

def major_minor_items_analyze(data):
    df = pd.DataFrame(data)
    major_items = df.sort_values(by='quantity', ascending=False).head(5).to_dict(orient='records')
    minor_items = df.sort_values(by='quantity', ascending=True).head(5).to_dict(orient='records')
    
    return { "major_items" : major_items, "minor_items" : minor_items }
