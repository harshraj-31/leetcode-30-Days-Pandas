import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    unique = activities.drop_duplicates()
    result = unique.groupby('sell_date', as_index=False).agg(
        num_sold=('product', 'size'),
        products=('product', lambda x: ','.join(sorted(x)))
    )
    return result