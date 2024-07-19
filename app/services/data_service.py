import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import io 
import base64

def analyze_data(data):
    df = pd.DataFrame(data)
    summary = df.groupby('product_id')['quantity'].sum().reset_index().to_dict(orient='records')
    
    plt.figure()
    sns.barplot(x='product_id', y='quantity', data=df.groupby('product_id')['quantity'].sum().reset_index())
    plt.title('Cantidad de productos vendidos')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    return { 'summary' : summary, 'plot' : plot_url }