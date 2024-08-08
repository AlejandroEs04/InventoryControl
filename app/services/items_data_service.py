import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import io 
import base64

def items_analyze(data):
    df = pd.DataFrame(data)

    summary = df.groupby('item_id')['quantity'].sum().reset_index().to_dict('records')
    
    plt.figure()
    sns.barplot(x="item_id", y="quantity", data=df.groupby('item_id')['quantity'].sum().reset_index())
    plt.title('Products total quantity for sales')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode() 
    
    return summary, plot_url

def items_analyze_by_period(data):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    
    grouped = df.groupby([df['date'].dt.to_period('M'), 'item_id']).agg({'quantity': 'sum'}).reset_index()
    grouped['date'] = grouped['date'].astype(str)
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='quantity', hue='item_id', data=grouped, marker='o')
    plt.title('Ventas por Producto y Período')
    plt.xlabel('Date')
    plt.ylabel('Quantity')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    return grouped.to_dict(orient='records'), plot_url

def major_minor_items_analyze(data):
    df = pd.DataFrame(data)
    major_items = df.sort_values(by='quantity', ascending=False).to_dict(orient='records')
    minor_items = df.sort_values(by='quantity', ascending=True).to_dict(orient='records')
    
    return { "major_items" : major_items, "minor_items" : minor_items }