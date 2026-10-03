import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    no_orders = customers[~customers['id'].isin(orders['customerId'])]
    return no_orders[['name']].rename(columns={'name': 'Customers'})