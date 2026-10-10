import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_ids = company.loc[company['name'] == 'RED', 'com_id']
    red_sellers = orders.loc[orders['com_id'].isin(red_ids), 'sales_id']
    return sales_person.loc[~sales_person['sales_id'].isin(red_sellers), ['name']]