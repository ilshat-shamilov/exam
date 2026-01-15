import pandas as pd
import yaml

users = pd.read_csv('users.csv')
orders = pd.read_json('orders.json')

total_spent = orders.groupby('user_id')['amount'].sum().reset_index()
total_spent.columns = ['id', 'total_spent']
result = pd.merge(users, total_spent, on='id')
top_users = result[result['total_spent'] > 1000]
output_data = top_users[['id', 'name', 'total_spent']].to_dict('records')

with open('top_users.yaml', 'w', encoding="utf-8") as f:
    yaml.safe_dump(output_data, f, allow_unicode=True)