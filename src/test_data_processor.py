import pandas as pd
import numpy as np
from data_processor import generate_dummy_data, analyze_sales_by_category

def test_generate_dummy_data():
    df = generate_dummy_data(num_rows=5)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert all(col in df.columns for col in ['product_id', 'category', 'price', 'quantity', 'transaction_date'])

def test_analyze_sales_by_category():
    data = {
        'product_id': [1, 2, 3, 4, 5],
        'category': ['Books', 'Clothing', 'Books', 'Food', 'Clothing'],
        'price': [10.0, 20.0, 15.0, 25.0, 30.0],
        'quantity': [2, 1, 3, 2, 1],
        'transaction_date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
    }
    df = pd.DataFrame(data)
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    sales_summary = analyze_sales_by_category(df)

    assert isinstance(sales_summary, pd.DataFrame)
    assert all(col in sales_summary.columns for col in ['category', 'total_sales_sum', 'average_sale_price', 'number_of_transactions'])
    
    # Check specific values
    books_summary = sales_summary[sales_summary['category'] == 'Books']
    assert books_summary['total_sales_sum'].iloc[0] == (10.0 * 2) + (15.0 * 3)
    assert books_summary['number_of_transactions'].iloc[0] == 2

    clothing_summary = sales_summary[sales_summary['category'] == 'Clothing']
    assert clothing_summary['total_sales_sum'].iloc[0] == (20.0 * 1) + (30.0 * 1)
    assert clothing_summary['number_of_transactions'].iloc[0] == 2

    food_summary = sales_summary[sales_summary['category'] == 'Food']
    assert food_summary['total_sales_sum'].iloc[0] == (25.0 * 2)
    assert food_summary['number_of_transactions'].iloc[0] == 1

if __name__ == '__main__':
    test_generate_dummy_data()
    test_analyze_sales_by_category()
    print('All tests passed!')

