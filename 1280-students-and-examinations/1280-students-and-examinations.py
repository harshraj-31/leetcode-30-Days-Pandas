import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    grid = students.merge(subjects, how='cross')
    counts = examinations.groupby(['student_id', 'subject_name'], as_index=False, sort=False).size()
    result = grid.merge(counts, on=['student_id', 'subject_name'], how='left')
    result['attended_exams'] = result['size'].fillna(0).astype(int)
    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']].sort_values(['student_id', 'subject_name'])