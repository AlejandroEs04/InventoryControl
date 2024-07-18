import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import io 
import base64

def analyze_data(data):
    df = pd.DataFrame(data)
    summary = df.describe().to_dict()
    
    plt.figure()
    sns.barplot(x='product', y='value', data=df)
    plt.title('Ventas por producto')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    return { 'summary' : summary, 'plot' : plot_url }