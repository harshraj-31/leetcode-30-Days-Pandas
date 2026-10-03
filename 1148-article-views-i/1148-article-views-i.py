import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    own_views = views[views['author_id'] == views['viewer_id']]
    authors = own_views[['author_id']].drop_duplicates()
    authors = authors.rename(columns={'author_id': 'id'})
    return authors.sort_values(by='id')