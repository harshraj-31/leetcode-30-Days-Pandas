import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = teacher.groupby('teacher_id', as_index=False, sort=False)['subject_id'].nunique()
    return result.rename(columns={'subject_id': 'cnt'})