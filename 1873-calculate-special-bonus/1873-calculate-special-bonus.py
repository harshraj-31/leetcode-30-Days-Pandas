import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    gets_bonus = (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M'))

    employees['bonus'] = 0
    employees.loc[gets_bonus, 'bonus'] = employees.loc[gets_bonus, 'salary']

    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')