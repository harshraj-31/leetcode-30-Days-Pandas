import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    has_diab1 = patients['conditions'].str.contains(r'(^| )DIAB1')
    return patients[has_diab1]