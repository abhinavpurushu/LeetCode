import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:

    # Pivot the table with 'month' as index, 'city' as columns, and 'temperature' as values
    return weather.pivot(index='month', columns='city', values='temperature')
