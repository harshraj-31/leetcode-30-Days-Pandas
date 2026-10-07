import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    counts = courses['class'].value_counts(sort=False)
    return pd.DataFrame({'class': counts[counts >= 5].index})