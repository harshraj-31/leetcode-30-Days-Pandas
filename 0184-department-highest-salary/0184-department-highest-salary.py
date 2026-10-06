import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department = department.rename(columns={'id': 'departmentId', 'name': 'Department'})
    merged = employee.merge(department, on='departmentId')

    max_salary = merged.groupby('departmentId')['salary'].transform('max')
    top = merged[merged['salary'] == max_salary]

    top = top.rename(columns={'name': 'Employee', 'salary': 'Salary'})
    return top[['Department', 'Employee', 'Salary']]