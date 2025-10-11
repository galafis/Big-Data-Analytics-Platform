import pandas as pd
import numpy as np
import sys
from data_processor import generate_dummy_data, analyze_sales_by_category

def test_generate_dummy_data():
    """Testa a geração de dados dummy."""
    print("Testando geração de dados dummy...")
    
    # Teste básico
    df = generate_dummy_data(num_rows=5)
    assert isinstance(df, pd.DataFrame), "Resultado deve ser um DataFrame"
    assert len(df) == 5, "DataFrame deve ter 5 linhas"
    assert all(col in df.columns for col in ['product_id', 'category', 'price', 'quantity', 'transaction_date']), \
        "DataFrame deve conter todas as colunas necessárias"
    
    # Teste de valores inválidos
    try:
        generate_dummy_data(num_rows=-1)
        assert False, "Deveria lançar ValueError para num_rows negativo"
    except ValueError:
        pass
    
    try:
        generate_dummy_data(num_rows=0)
        assert False, "Deveria lançar ValueError para num_rows zero"
    except ValueError:
        pass
    
    print("✓ Teste de geração de dados passou!")

def test_analyze_sales_by_category():
    """Testa a análise de vendas por categoria."""
    print("Testando análise de vendas por categoria...")
    
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

    assert isinstance(sales_summary, pd.DataFrame), "Resultado deve ser um DataFrame"
    assert all(col in sales_summary.columns for col in ['category', 'total_sales_sum', 'average_sale_price', 'number_of_transactions']), \
        "DataFrame deve conter todas as colunas necessárias"
    
    # Check specific values
    books_summary = sales_summary[sales_summary['category'] == 'Books']
    assert books_summary['total_sales_sum'].iloc[0] == (10.0 * 2) + (15.0 * 3), \
        "Total de vendas de Books deve ser 65.0"
    assert books_summary['number_of_transactions'].iloc[0] == 2, \
        "Número de transações de Books deve ser 2"

    clothing_summary = sales_summary[sales_summary['category'] == 'Clothing']
    assert clothing_summary['total_sales_sum'].iloc[0] == (20.0 * 1) + (30.0 * 1), \
        "Total de vendas de Clothing deve ser 50.0"
    assert clothing_summary['number_of_transactions'].iloc[0] == 2, \
        "Número de transações de Clothing deve ser 2"

    food_summary = sales_summary[sales_summary['category'] == 'Food']
    assert food_summary['total_sales_sum'].iloc[0] == (25.0 * 2), \
        "Total de vendas de Food deve ser 50.0"
    assert food_summary['number_of_transactions'].iloc[0] == 1, \
        "Número de transações de Food deve ser 1"
    
    # Teste com DataFrame vazio
    try:
        analyze_sales_by_category(pd.DataFrame())
        assert False, "Deveria lançar ValueError para DataFrame vazio"
    except ValueError:
        pass
    
    # Teste com colunas faltando
    try:
        analyze_sales_by_category(pd.DataFrame({'category': ['A', 'B']}))
        assert False, "Deveria lançar ValueError para DataFrame com colunas faltando"
    except ValueError:
        pass
    
    print("✓ Teste de análise de vendas passou!")

def test_integration():
    """Testa o fluxo completo de geração e análise."""
    print("Testando integração completa...")
    
    df = generate_dummy_data(num_rows=100)
    summary = analyze_sales_by_category(df)
    
    assert not summary.empty, "Resumo não deve estar vazio"
    assert summary['total_sales_sum'].sum() > 0, "Total de vendas deve ser positivo"
    
    print("✓ Teste de integração passou!")

if __name__ == '__main__':
    try:
        test_generate_dummy_data()
        test_analyze_sales_by_category()
        test_integration()
        print('\n✅ Todos os testes passaram!')
        sys.exit(0)
    except AssertionError as e:
        print(f'\n❌ Teste falhou: {e}', file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f'\n❌ Erro inesperado: {e}', file=sys.stderr)
        sys.exit(1)

