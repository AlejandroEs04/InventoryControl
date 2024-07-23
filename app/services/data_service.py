import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import io 
import base64

def analyze_total_products(data):
    df = pd.DataFrame(data)
    
    summary = df.groupby('item_id')['quantity'].sum().reset_index().to_dict(orient='records')
    
    plt.figure()
    sns.barplot(x='item_id', y='quantity', data=df.groupby('item_id')['quantity'].sum().reset_index())
    plt.title('Cantidad de productos vendidos')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    return { 'summary' : summary, 'plot' : plot_url }

def analyze_action_by_period(data):
    df = pd.DataFrame(data)
    
    df['date'] = pd.to_datetime(df['date'])
    
    actions_by_period = df.groupby(df['date'].dt.to_period('M')).agg({
        'quantity': 'sum',
        'action_id': 'count'
    }).reset_index()
    
    actions_by_period.columns = ['date', 'total_quantity', 'total_actions']
    actions_by_period['date'] = actions_by_period['date'].astype(str)
    
    product_sales_by_period = df.groupby([df['date'].dt.to_period('M'), 'item_id'])['quantity'].sum().reset_index()
    product_sales_by_period['date'] = product_sales_by_period['date'].astype(str)
    
    detailed_sales = product_sales_by_period.groupby('date').apply(lambda x: x[['item_id', 'quantity']].to_dict(orient='records')).reset_index()
    detailed_sales.columns = ['date', 'details']
    
    actions_by_period = actions_by_period.merge(detailed_sales, on='date')
    
    plt.figure()
    sns.lineplot(x='date', y='total_quantity', data=actions_by_period, label='Total Quantity')
    sns.lineplot(x='date', y='total_actions', data=actions_by_period, label='Total Actions')
    plt.title('Ventas por Periodo')
    plt.legend()
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
        
    return {
        'actions_by_period': actions_by_period.to_dict(orient='records'),
        'plot': plot_url
    }