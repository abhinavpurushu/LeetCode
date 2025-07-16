import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where both low_fats and recyclable are 'Y'
    result = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    
    # Return only the product_id column
    return result[['product_id']]
