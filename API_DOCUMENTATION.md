# API Documentation

## Big Data Analytics Platform - Function Reference

This document provides detailed documentation for all public functions in the Big Data Analytics Platform.

---

## Table of Contents

- [Data Generation](#data-generation)
  - [generate_dummy_data](#generate_dummy_data)
- [Data Analysis](#data-analysis)
  - [analyze_sales_by_category](#analyze_sales_by_category)
- [Data Export](#data-export)
  - [save_to_csv](#save_to_csv)
  - [save_to_json](#save_to_json)
  - [export_data](#export_data)

---

## Data Generation

### generate_dummy_data

```python
def generate_dummy_data(num_rows: int = 100) -> pd.DataFrame
```

Generates dummy sales data for testing and demonstration purposes.

**Parameters:**
- `num_rows` (int, optional): Number of data rows to generate. Default: 100
  - Must be a positive integer
  - Recommended range: 10-10000 for reasonable performance

**Returns:**
- `pd.DataFrame`: DataFrame with synthetic sales data containing:
  - `product_id` (int): Product identifier (1-9)
  - `category` (str): Product category (Electronics, Clothing, Books, Food)
  - `price` (float): Unit price ($10-$500)
  - `quantity` (int): Quantity sold (1-9 units)
  - `transaction_date` (datetime): Transaction date (2023 calendar year)

**Raises:**
- `ValueError`: If num_rows is not a positive integer

**Example:**
```python
from data_processor import generate_dummy_data

# Generate 50 transactions
df = generate_dummy_data(num_rows=50)
print(df.head())
```

**Notes:**
- Uses fixed random seed (42) for reproducible results
- Data is uniformly distributed across categories
- Dates are randomly distributed throughout 2023

---

## Data Analysis

### analyze_sales_by_category

```python
def analyze_sales_by_category(df: pd.DataFrame) -> pd.DataFrame
```

Analyzes sales data aggregated by product category.

**Parameters:**
- `df` (pd.DataFrame): DataFrame with sales data containing required columns:
  - `price` (numeric): Unit price
  - `quantity` (numeric): Quantity sold
  - `category` (str): Product category

**Returns:**
- `pd.DataFrame`: Summary DataFrame with columns:
  - `category` (str): Product category name
  - `total_sales_sum` (float): Total revenue for category
  - `average_sale_price` (float): Average transaction value
  - `number_of_transactions` (int): Count of transactions

**Raises:**
- `ValueError`: If DataFrame is missing required columns
- `ValueError`: If DataFrame is empty

**Example:**
```python
from data_processor import generate_dummy_data, analyze_sales_by_category

df = generate_dummy_data(num_rows=100)
summary = analyze_sales_by_category(df)
print(summary)
```

**Notes:**
- Calculates total_sales as price × quantity for each transaction
- Groups data by category and applies aggregation functions
- Returns sorted DataFrame by category name

---

## Data Export

### save_to_csv

```python
def save_to_csv(df: pd.DataFrame, output_path: str) -> None
```

Saves DataFrame to CSV file.

**Parameters:**
- `df` (pd.DataFrame): DataFrame to save
- `output_path` (str): File path for output CSV
  - Parent directories will be created if they don't exist
  - Example: `'data/results.csv'`

**Returns:**
- None

**Raises:**
- `IOError`: If file cannot be written

**Example:**
```python
from data_processor import generate_dummy_data, save_to_csv

df = generate_dummy_data(num_rows=50)
save_to_csv(df, 'output/my_data.csv')
```

**Notes:**
- Automatically creates parent directories
- Does not include DataFrame index in output
- Logs success message with file path

---

### save_to_json

```python
def save_to_json(df: pd.DataFrame, output_path: str) -> None
```

Saves DataFrame to JSON file.

**Parameters:**
- `df` (pd.DataFrame): DataFrame to save
- `output_path` (str): File path for output JSON
  - Parent directories will be created if they don't exist
  - Example: `'data/results.json'`

**Returns:**
- None

**Raises:**
- `IOError`: If file cannot be written

**Example:**
```python
from data_processor import generate_dummy_data, save_to_json

df = generate_dummy_data(num_rows=50)
save_to_json(df, 'output/my_data.json')
```

**Notes:**
- Uses 'records' orientation (list of dictionaries)
- Pretty-printed with 2-space indentation
- Automatically creates parent directories
- Logs success message with file path

---

### export_data

```python
def export_data(df: pd.DataFrame, base_path: str, formats: list = ['csv', 'json']) -> None
```

Exports DataFrame to multiple file formats simultaneously.

**Parameters:**
- `df` (pd.DataFrame): DataFrame to export
- `base_path` (str): Base file path without extension
  - Example: `'data/sales_summary'` → creates `sales_summary.csv` and `sales_summary.json`
- `formats` (list, optional): List of format strings. Default: `['csv', 'json']`
  - Supported formats: `'csv'`, `'json'`
  - Invalid formats are logged as warnings and skipped

**Returns:**
- None

**Raises:**
- `IOError`: If any file cannot be written (via save functions)

**Example:**
```python
from data_processor import generate_dummy_data, analyze_sales_by_category, export_data

df = generate_dummy_data(num_rows=100)
summary = analyze_sales_by_category(df)

# Export to both CSV and JSON
export_data(summary, 'output/report', formats=['csv', 'json'])

# Export only to CSV
export_data(summary, 'output/report_csv_only', formats=['csv'])
```

**Notes:**
- Convenient wrapper around individual save functions
- Automatically appends appropriate file extensions
- Creates all requested formats in one call
- Useful for ensuring data is available in multiple formats

---

## Complete Workflow Example

Here's a complete example showing all functions working together:

```python
from data_processor import (
    generate_dummy_data,
    analyze_sales_by_category,
    export_data
)

# Step 1: Generate data
print("Generating data...")
transactions = generate_dummy_data(num_rows=200)
print(f"Generated {len(transactions)} transactions")

# Step 2: Analyze data
print("Analyzing sales...")
sales_summary = analyze_sales_by_category(transactions)
print(sales_summary)

# Step 3: Export results
print("Exporting results...")
export_data(sales_summary, 'data/analysis_results', formats=['csv', 'json'])
print("Done! Files saved to:")
print("  - data/analysis_results.csv")
print("  - data/analysis_results.json")
```

---

## Type Hints

All functions include type hints for better IDE support and type checking:

```python
from typing import Optional, Literal
import pandas as pd

def generate_dummy_data(num_rows: int = 100) -> pd.DataFrame:
    ...

def analyze_sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    ...

def save_to_csv(df: pd.DataFrame, output_path: str) -> None:
    ...

def save_to_json(df: pd.DataFrame, output_path: str) -> None:
    ...

def export_data(df: pd.DataFrame, base_path: str, formats: list = ['csv', 'json']) -> None:
    ...
```

---

## Logging

All functions use structured logging. Enable detailed logging with:

```python
import logging

# Set log level to INFO to see all operations
logging.basicConfig(level=logging.INFO)

# Set log level to DEBUG for even more detail
logging.basicConfig(level=logging.DEBUG)
```

Example log output:
```
2025-10-13 16:04:44,315 - data_processor - INFO - Gerando 50 linhas de dados dummy...
2025-10-13 16:04:44,318 - data_processor - INFO - Dados gerados com sucesso: 50 linhas, 5 colunas
2025-10-13 16:04:44,323 - data_processor - INFO - Analisando vendas por categoria para 50 registros...
2025-10-13 16:04:44,325 - data_processor - INFO - Análise completa: 4 categorias encontradas
```

---

## Error Handling

All functions include comprehensive error handling:

- **Input Validation**: Parameters are validated before processing
- **Descriptive Errors**: Clear error messages explain what went wrong
- **Logging**: All errors are logged before raising exceptions
- **Graceful Failures**: Functions fail fast with informative messages

Example error handling:

```python
from data_processor import generate_dummy_data

try:
    # This will raise ValueError
    df = generate_dummy_data(num_rows=-10)
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: num_rows deve ser um inteiro positivo
```

---

## Version Information

- **API Version**: 2.2.0
- **Python Required**: 3.7+
- **Dependencies**: 
  - pandas >= 2.0.0
  - numpy >= 1.20.0

---

## Contributing

For information on contributing to this project, see [CONTRIBUTING.md](CONTRIBUTING.md).

For bug reports and feature requests, please open an issue on GitHub.
