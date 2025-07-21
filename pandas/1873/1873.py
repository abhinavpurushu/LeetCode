import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    # Apply the condition: odd employee_id and name does not start with 'M'
    employees['bonus'] = employees.apply(lambda row: row['salary'] if row['employee_id'] % 2 == 1 and not row['name'].startswith('M') else 0, axis=1)
    
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')
