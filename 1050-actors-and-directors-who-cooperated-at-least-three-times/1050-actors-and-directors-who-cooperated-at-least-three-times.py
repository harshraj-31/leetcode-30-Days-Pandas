import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    counts = actor_director.groupby(['actor_id', 'director_id'], as_index=False, sort=False).size()
    return counts[counts['size'] >= 3][['actor_id', 'director_id']]