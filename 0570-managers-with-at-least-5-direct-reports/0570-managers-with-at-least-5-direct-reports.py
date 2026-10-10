import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee['managerId'].value_counts(sort=False)
    manager_ids = counts[counts >= 5].index
    return employee.loc[employee['id'].isin(manager_ids), ['name']]