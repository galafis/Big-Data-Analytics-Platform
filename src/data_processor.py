
import pandas as pd
import numpy as np

def generate_dummy_data(num_rows=100):
    """Gera dados dummy para simular um dataset de vendas."""
    np.random.seed(42)
    data = {
        'product_id': np.random.randint(1, 10, num_rows),
        'category': np.random.choice(['Eletronics', 'Clothing', 'Books', 'Food'], num_rows),
        'price': np.round(np.random.uniform(10, 500, num_rows), 2),
        'quantity': np.random.randint(1, 10, num_rows),
        'transaction_date': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 365, num_rows), unit='D')
    }
    return pd.DataFrame(data)

def analyze_sales_by_category(df):
    """Analisa as vendas por categoria de produto."""
    df['total_sales'] = df['price'] * df['quantity']
    sales_summary = df.groupby('category')['total_sales'].agg(['sum', 'mean', 'count']).reset_index()
    sales_summary.columns = ['category', 'total_sales_sum', 'average_sale_price', 'number_of_transactions']
    return sales_summary

def main():
    print("Gerando dados dummy...")
    df = generate_dummy_data()
    print("Dados gerados:")
    print(df.head())

    print("\nAnalisando vendas por categoria...")
    sales_summary = analyze_sales_by_category(df)
    print("Resumo de vendas por categoria:")
    print(sales_summary)

    # Salvar o resumo em um arquivo CSV para demonstração
    output_path = 'data/sales_summary.csv'
    sales_summary.to_csv(output_path, index=False)
    print(f"\nResumo de vendas salvo em: {output_path}")

if __name__ == "__main__":
    main()

