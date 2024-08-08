import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import io 
import base64

def actions_analyse(data):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])

    # actions by period
    actions_by_month = df.groupby(df['date'].dt.to_period('M')).size().reset_index()
    actions_by_month.columns = ['period', 'actions_quantity']
    actions_by_month['period'] = actions_by_month['period'].astype(str)
    
    # actions amounts by period 
    amount_by_month = df.groupby(df['date'].dt.to_period('M'))['amount'].sum().reset_index()
    amount_by_month.columns = ['period', 'total_amount'] 
    amount_by_month['period'] = amount_by_month['period'].astype(str)
    
    return actions_by_month.to_dict(orient='records'), amount_by_month.to_dict(orient='records')