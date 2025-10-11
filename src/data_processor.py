
import pandas as pd
import numpy as np
import os
import sys

def generate_dummy_data(num_rows=100):
    """
    Gera dados dummy para simular um dataset de vendas.
    
    Args:
        num_rows (int): Número de linhas de dados a gerar. Padrão: 100
        
    Returns:
        pd.DataFrame: DataFrame com dados de vendas simulados
        
    Raises:
        ValueError: Se num_rows não for um inteiro positivo
    """
    if not isinstance(num_rows, int) or num_rows <= 0:
        raise ValueError("num_rows deve ser um inteiro positivo")
    
    np.random.seed(42)
    data = {
        'product_id': np.random.randint(1, 10, num_rows),
        'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Food'], num_rows),
        'price': np.round(np.random.uniform(10, 500, num_rows), 2),
        'quantity': np.random.randint(1, 10, num_rows),
        'transaction_date': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 365, num_rows), unit='D')
    }
    return pd.DataFrame(data)

def analyze_sales_by_category(df):
    """
    Analisa as vendas por categoria de produto.
    
    Args:
        df (pd.DataFrame): DataFrame com dados de vendas contendo colunas 'price', 'quantity', e 'category'
        
    Returns:
        pd.DataFrame: Resumo de vendas por categoria
        
    Raises:
        ValueError: Se o DataFrame não contiver as colunas necessárias
    """
    required_columns = ['price', 'quantity', 'category']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        raise ValueError(f"DataFrame está faltando as colunas necessárias: {missing_columns}")
    
    if df.empty:
        raise ValueError("DataFrame está vazio")
    
    df['total_sales'] = df['price'] * df['quantity']
    sales_summary = df.groupby('category')['total_sales'].agg(['sum', 'mean', 'count']).reset_index()
    sales_summary.columns = ['category', 'total_sales_sum', 'average_sale_price', 'number_of_transactions']
    return sales_summary

def main():
    try:
        print("Gerando dados dummy...")
        df = generate_dummy_data()
        print("Dados gerados:")
        print(df.head())

        print("\nAnalisando vendas por categoria...")
        sales_summary = analyze_sales_by_category(df)
        print("Resumo de vendas por categoria:")
        print(sales_summary)

        # Criar diretório data se não existir
        os.makedirs('data', exist_ok=True)
        
        # Salvar o resumo em um arquivo CSV para demonstração
        output_path = 'data/sales_summary.csv'
        sales_summary.to_csv(output_path, index=False)
        print(f"\nResumo de vendas salvo em: {output_path}")
        
        return 0
        
    except Exception as e:
        print(f"Erro durante a execução: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())

