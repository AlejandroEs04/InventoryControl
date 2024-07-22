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
    
    # Group sales per year and month
    sales_by_period = df.groupby(df['date'].dt.to_period('M'))['quantity'].sum().reset_index()
    sales_by_period['date'] = sales_by_period['date'].astype(str)
    
    plt.figure()
    sns.lineplot(x='date', y='quantity', data=sales_by_period)
    plt.title('Ventas por Periodo')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
        
    return { 'sales_by_period': sales_by_period.to_dict(orient='records'), 'plot' : plot_url }