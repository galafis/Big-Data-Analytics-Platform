
import pandas as pd
import numpy as np
import os
import sys
import logging
import json
from typing import Optional, Literal

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def generate_dummy_data(num_rows: int = 100) -> pd.DataFrame:
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
        logger.error(f"Valor inválido para num_rows: {num_rows}. Deve ser um inteiro positivo.")
        raise ValueError("num_rows deve ser um inteiro positivo")
    
    logger.info(f"Gerando {num_rows} linhas de dados dummy...")
    np.random.seed(42)
    data = {
        'product_id': np.random.randint(1, 10, num_rows),
        'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Food'], num_rows),
        'price': np.round(np.random.uniform(10, 500, num_rows), 2),
        'quantity': np.random.randint(1, 10, num_rows),
        'transaction_date': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 365, num_rows), unit='D')
    }
    df = pd.DataFrame(data)
    logger.info(f"Dados gerados com sucesso: {len(df)} linhas, {len(df.columns)} colunas")
    return df

def analyze_sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
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
        logger.error(f"DataFrame está faltando colunas necessárias: {missing_columns}")
        raise ValueError(f"DataFrame está faltando as colunas necessárias: {missing_columns}")
    
    if df.empty:
        logger.error("DataFrame está vazio")
        raise ValueError("DataFrame está vazio")
    
    logger.info(f"Analisando vendas por categoria para {len(df)} registros...")
    df['total_sales'] = df['price'] * df['quantity']
    sales_summary = df.groupby('category')['total_sales'].agg(['sum', 'mean', 'count']).reset_index()
    sales_summary.columns = ['category', 'total_sales_sum', 'average_sale_price', 'number_of_transactions']
    logger.info(f"Análise completa: {len(sales_summary)} categorias encontradas")
    return sales_summary

def save_to_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    Salva DataFrame em arquivo CSV.
    
    Args:
        df (pd.DataFrame): DataFrame a ser salvo
        output_path (str): Caminho do arquivo de saída
        
    Raises:
        IOError: Se houver erro ao salvar o arquivo
    """
    try:
        # Criar diretório se não existir
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        logger.info(f"Dados salvos com sucesso em: {output_path}")
    except Exception as e:
        logger.error(f"Erro ao salvar arquivo CSV: {e}")
        raise IOError(f"Erro ao salvar arquivo: {e}")

def save_to_json(df: pd.DataFrame, output_path: str) -> None:
    """
    Salva DataFrame em arquivo JSON.
    
    Args:
        df (pd.DataFrame): DataFrame a ser salvo
        output_path (str): Caminho do arquivo de saída
        
    Raises:
        IOError: Se houver erro ao salvar o arquivo
    """
    try:
        # Criar diretório se não existir
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_json(output_path, orient='records', indent=2)
        logger.info(f"Dados salvos com sucesso em JSON: {output_path}")
    except Exception as e:
        logger.error(f"Erro ao salvar arquivo JSON: {e}")
        raise IOError(f"Erro ao salvar arquivo JSON: {e}")

def export_data(df: pd.DataFrame, base_path: str, formats: list = ['csv', 'json']) -> None:
    """
    Exporta DataFrame em múltiplos formatos.
    
    Args:
        df (pd.DataFrame): DataFrame a ser exportado
        base_path (str): Caminho base para os arquivos (sem extensão)
        formats (list): Lista de formatos ('csv', 'json')
    """
    for fmt in formats:
        if fmt == 'csv':
            save_to_csv(df, f"{base_path}.csv")
        elif fmt == 'json':
            save_to_json(df, f"{base_path}.json")
        else:
            logger.warning(f"Formato não suportado: {fmt}")

def main() -> int:
    try:
        logger.info("Iniciando processamento de dados...")
        print("Gerando dados dummy...")
        df = generate_dummy_data()
        print("Dados gerados:")
        print(df.head())

        print("\nAnalisando vendas por categoria...")
        sales_summary = analyze_sales_by_category(df)
        print("Resumo de vendas por categoria:")
        print(sales_summary)
        
        # Exportar o resumo em múltiplos formatos
        base_output_path = 'data/sales_summary'
        export_data(sales_summary, base_output_path, formats=['csv', 'json'])
        print(f"\nResumo de vendas exportado para:")
        print(f"  - {base_output_path}.csv")
        print(f"  - {base_output_path}.json")
        
        logger.info("Processamento concluído com sucesso")
        return 0
        
    except Exception as e:
        logger.error(f"Erro durante a execução: {e}")
        print(f"Erro durante a execução: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())

