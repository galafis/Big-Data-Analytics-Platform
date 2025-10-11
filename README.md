# Big Data Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-orange.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-blue.svg)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/galafis/Big-Data-Analytics-Platform/actions)

![Big Data Analytics Platform](https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&h=400&fit=crop&q=80)

*Uma plataforma moderna de análise de Big Data para processamento e análise de grandes volumes de dados*

---

## 📋 Índice / Table of Contents

- [🇧🇷 Português](#-português)
  - [Visão Geral](#visão-geral)
  - [Funcionalidades](#funcionalidades)
  - [Arquitetura](#arquitetura)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [Como Usar](#como-usar)
  - [Exemplos de Uso](#exemplos-de-uso)
  - [Testes](#testes)
  - [Solução de Problemas](#solução-de-problemas)
  - [Melhorias Futuras](#melhorias-futuras)
- [🇬🇧 English](#-english)
  - [Overview](#overview)
  - [Features](#features)
  - [Architecture](#architecture)
  - [Technologies Used](#technologies-used)
  - [Project Structure](#project-structure)
  - [How to Use](#how-to-use)
  - [Usage Examples](#usage-examples)
  - [Testing](#testing)
  - [Troubleshooting](#troubleshooting)
  - [Future Enhancements](#future-enhancements)

## 🇧🇷 Português

### Visão Geral

Este repositório apresenta uma **Plataforma de Análise de Big Data** em estágio inicial, focada na demonstração de processamento e análise de grandes volumes de dados. O objetivo é fornecer uma base funcional para explorar conceitos de Big Data, desde a ingestão simulada de dados até a geração de *insights* através de análises. O projeto é modular e extensível, permitindo a integração de diversas fontes de dados e ferramentas de visualização.

### Funcionalidades

-   **Geração de Dados Dummy:** Simula a criação de grandes conjuntos de dados transacionais.
-   **Processamento e Análise:** Realiza análises básicas de vendas por categoria, calculando somas, médias e contagens.
-   **Estrutura Modular:** Organização clara do código e dos dados para facilitar a compreensão e expansão.
-   **Interface Web:** Visualização de resultados através de uma interface web simples e responsiva.
-   **Testes Automatizados:** Suite de testes unitários para garantir a qualidade do código.
-   **CI/CD:** Integração contínua configurada com GitHub Actions.

### Arquitetura

O projeto segue uma arquitetura modular simples:

```
┌─────────────────┐
│  Data Generator │  ──→  Gera dados sintéticos de vendas
└─────────────────┘
         ↓
┌─────────────────┐
│  Data Processor │  ──→  Processa e analisa dados
└─────────────────┘
         ↓
┌─────────────────┐
│   CSV Output    │  ──→  Salva resultados em CSV
└─────────────────┘
         ↓
┌─────────────────┐
│  Web Interface  │  ──→  Visualiza dados na web
└─────────────────┘
```

**Fluxo de Dados:**
1. **Geração**: Dados sintéticos são criados usando NumPy
2. **Transformação**: Dados são processados com Pandas
3. **Análise**: Agregações e cálculos estatísticos
4. **Armazenamento**: Resultados salvos em formato CSV
5. **Visualização**: Interface web carrega e exibe os dados

### Tecnologias Utilizadas

| Categoria    | Tecnologia | Descrição                                    |
| :----------- | :--------- | :------------------------------------------- |
| **Linguagem**| Python     | Linguagem principal para processamento de dados. |
| **Bibliotecas**| Pandas     | Manipulação e análise de dados.              |
|              | NumPy      | Suporte a operações numéricas de alto desempenho. |
| **Web**      | HTML       | Estrutura da interface web.                  |
|              | CSS        | Estilização da interface web.                |

### Estrutura do Projeto

```
Big-Data-Analytics-Platform/
├── .github/                 # Configurações do GitHub (ex: Workflows, GitHub Pages)
│   └── workflows/           
│       └── test.yml         # GitHub Actions para testes automatizados
├── data/                    # Armazena dados processados e resultados de análises
│   └── sales_summary.csv    # Exemplo de resultado de análise (gerado)
├── src/                     # Código fonte principal
│   ├── data_processor.py    # Script para geração e análise de dados
│   └── test_data_processor.py # Testes unitários para o processador de dados
├── web/                     # Arquivos da interface web (GitHub Pages)
│   ├── index.html           # Página principal da plataforma
│   └── styles.css           # Estilos CSS para a página web
├── .gitignore               # Arquivos a serem ignorados pelo Git
├── CODE_OF_CONDUCT.md       # Código de Conduta
├── CONTRIBUTING.md          # Diretrizes para Contribuição
├── LICENSE                  # Licença do Projeto
├── README.md                # Este arquivo (documentação do projeto)
└── requirements.txt         # Dependências do Python
```

### Como Usar

Para configurar e executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/galafis/Big-Data-Analytics-Platform.git
    cd Big-Data-Analytics-Platform
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o processador de dados:**

    ```bash
    python3 src/data_processor.py
    ```

    Este script irá gerar dados dummy, realizar uma análise de vendas por categoria e salvar os resultados em `data/sales_summary.csv`.

5.  **Execute os testes (opcional):**

    ```bash
    python3 src/test_data_processor.py
    ```

### Exemplos de Uso

#### Gerando e Analisando Dados

```python
from src.data_processor import generate_dummy_data, analyze_sales_by_category

# Gerar 1000 linhas de dados de vendas
df = generate_dummy_data(num_rows=1000)
print(df.head())

# Analisar vendas por categoria
summary = analyze_sales_by_category(df)
print(summary)
```

#### Saída Esperada

```
Gerando dados dummy...
Dados gerados:
   product_id     category   price  quantity transaction_date
0           7        Books  134.42         5       2023-04-04
1           4  Electronics  130.97         6       2023-08-26
2           8        Books  351.19         3       2023-07-23
...

Analisando vendas por categoria...
Resumo de vendas por categoria:
      category  total_sales_sum  average_sale_price  number_of_transactions
0        Books         35543.39         1225.634138                      29
1     Clothing         32032.74         1525.368571                      21
2  Electronics         40168.57         1487.724815                      27
3         Food         37850.03         1645.653478                      23
```

### Testes

O projeto inclui uma suite completa de testes unitários:

```bash
# Executar todos os testes
python3 src/test_data_processor.py
```

**Cobertura de Testes:**
- ✅ Geração de dados dummy
- ✅ Validação de estrutura de dados
- ✅ Análise de vendas por categoria
- ✅ Cálculos de agregação
- ✅ Integridade dos resultados

### Solução de Problemas

#### Erro: "ModuleNotFoundError: No module named 'pandas'"

**Solução:** Certifique-se de que você instalou as dependências:
```bash
pip install -r requirements.txt
```

#### Erro: "FileNotFoundError: [Errno 2] No such file or directory: 'data/sales_summary.csv'"

**Solução:** Execute o processador de dados primeiro para gerar o arquivo CSV:
```bash
python3 src/data_processor.py
```

#### Erro de Permissão ao Salvar CSV

**Solução:** Verifique se o diretório `data/` existe e se você tem permissões de escrita:
```bash
mkdir -p data
chmod 755 data
```

### Melhorias Futuras

Roadmap de funcionalidades planejadas:

- [ ] **Suporte a múltiplas fontes de dados**
  - Integração com bancos de dados (PostgreSQL, MongoDB)
  - Leitura de arquivos CSV, JSON, Parquet
  - Conexão com APIs externas

- [ ] **Visualizações Avançadas**
  - Gráficos interativos com Plotly/Chart.js
  - Dashboard em tempo real
  - Mapas de calor e análises temporais

- [ ] **Machine Learning**
  - Previsão de vendas
  - Detecção de anomalias
  - Segmentação de clientes

- [ ] **Processamento Distribuído**
  - Integração com Apache Spark
  - Processamento em paralelo
  - Suporte a grandes volumes (>1GB)

- [ ] **API REST**
  - Endpoints para análise de dados
  - Autenticação e autorização
  - Documentação com Swagger

- [ ] **Melhorias de Qualidade**
  - Logging estruturado
  - Tratamento de erros robusto
  - Validação de dados de entrada
  - Métricas de performance

### GitHub Pages

A interface web básica (`web/index.html`) está configurada para ser servida via GitHub Pages. Você pode acessá-la em: `https://galafis.github.io/Big-Data-Analytics-Platform/`

#### 🎨 Preview da Interface Web

![Web Dashboard](https://github.com/user-attachments/assets/6a4f287f-513d-4cd6-85f0-416f9517620b)

**Recursos do Dashboard:**
- 📊 Estatísticas em tempo real (categorias, transações, receita, média de vendas)
- 📋 Tabela interativa com dados de vendas por categoria
- 🔄 Ordenação de colunas com um clique
- 📱 Design responsivo para mobile e desktop
- ⚡ Carregamento assíncrono de dados
- ❗ Tratamento de erros com mensagens amigáveis

### Contribuição

Contribuições são bem-vindas! Por favor, leia o `CONTRIBUTING.md` para mais detalhes.

### Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

### Autor

Feito com ❤️ por Gabriel Demetrios Lafis.

---

## 🇬🇧 English

### Overview

This repository presents an initial **Big Data Analytics Platform**, focused on demonstrating the processing and analysis of large data volumes. The goal is to provide a functional foundation for exploring Big Data concepts, from simulated data ingestion to generating insights through analysis. The project is modular and extensible, allowing the integration of various data sources and visualization tools.

### Features

-   **Dummy Data Generation:** Simulates the creation of large transactional datasets.
-   **Processing and Analysis:** Performs basic sales analysis by category, calculating sums, averages, and counts.
-   **Modular Structure:** Clear organization of code and data to facilitate understanding and expansion.
-   **Web Interface:** Result visualization through a simple and responsive web interface.
-   **Automated Tests:** Unit test suite to ensure code quality.
-   **CI/CD:** Continuous integration configured with GitHub Actions.

### Architecture

The project follows a simple modular architecture:

```
┌─────────────────┐
│  Data Generator │  ──→  Generates synthetic sales data
└─────────────────┘
         ↓
┌─────────────────┐
│  Data Processor │  ──→  Processes and analyzes data
└─────────────────┘
         ↓
┌─────────────────┐
│   CSV Output    │  ──→  Saves results to CSV
└─────────────────┘
         ↓
┌─────────────────┐
│  Web Interface  │  ──→  Visualizes data on web
└─────────────────┘
```

**Data Flow:**
1. **Generation**: Synthetic data is created using NumPy
2. **Transformation**: Data is processed with Pandas
3. **Analysis**: Aggregations and statistical calculations
4. **Storage**: Results saved in CSV format
5. **Visualization**: Web interface loads and displays the data

### Technologies Used

| Category    | Technology | Description                                    |
| :----------- | :--------- | :------------------------------------------- |
| **Language** | Python     | Main language for data processing.           |
| **Libraries**| Pandas     | Data manipulation and analysis.              |
|              | NumPy      | High-performance numerical operations support. |
| **Web**      | HTML       | Web interface structure.                     |
|              | CSS        | Web interface styling.                       |

### Project Structure

```
Big-Data-Analytics-Platform/
├── .github/                 # GitHub configurations (e.g., Workflows, GitHub Pages)
│   └── workflows/           
│       └── test.yml         # GitHub Actions for automated testing
├── data/                    # Stores processed data and analysis results
│   └── sales_summary.csv    # Example of analysis result (generated)
├── src/                     # Main source code
│   ├── data_processor.py    # Script for data generation and analysis
│   └── test_data_processor.py # Unit tests for the data processor
├── web/                     # Web interface files (GitHub Pages)
│   ├── index.html           # Main platform page
│   └── styles.css           # CSS styles for the web page
├── .gitignore               # Files to be ignored by Git
├── CODE_OF_CONDUCT.md       # Code of Conduct
├── CONTRIBUTING.md          # Contribution Guidelines
├── LICENSE                  # Project License
├── README.md                # This file (project documentation)
└── requirements.txt         # Python dependencies
```

### How to Use

To set up and run this project locally, follow the steps below:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/galafis/Big-Data-Analytics-Platform.git
    cd Big-Data-Analytics-Platform
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the data processor:**

    ```bash
    python3 src/data_processor.py
    ```

    This script will generate dummy data, perform a sales analysis by category, and save the results to `data/sales_summary.csv`.

5.  **Run tests (optional):**

    ```bash
    python3 src/test_data_processor.py
    ```

### Usage Examples

#### Generating and Analyzing Data

```python
from src.data_processor import generate_dummy_data, analyze_sales_by_category

# Generate 1000 rows of sales data
df = generate_dummy_data(num_rows=1000)
print(df.head())

# Analyze sales by category
summary = analyze_sales_by_category(df)
print(summary)
```

#### Expected Output

```
Gerando dados dummy...
Dados gerados:
   product_id     category   price  quantity transaction_date
0           7        Books  134.42         5       2023-04-04
1           4  Electronics  130.97         6       2023-08-26
2           8        Books  351.19         3       2023-07-23
...

Analisando vendas por categoria...
Resumo de vendas por categoria:
      category  total_sales_sum  average_sale_price  number_of_transactions
0        Books         35543.39         1225.634138                      29
1     Clothing         32032.74         1525.368571                      21
2  Electronics         40168.57         1487.724815                      27
3         Food         37850.03         1645.653478                      23
```

### Testing

The project includes a complete unit test suite:

```bash
# Run all tests
python3 src/test_data_processor.py
```

**Test Coverage:**
- ✅ Dummy data generation
- ✅ Data structure validation
- ✅ Sales analysis by category
- ✅ Aggregation calculations
- ✅ Results integrity

### Troubleshooting

#### Error: "ModuleNotFoundError: No module named 'pandas'"

**Solution:** Make sure you have installed the dependencies:
```bash
pip install -r requirements.txt
```

#### Error: "FileNotFoundError: [Errno 2] No such file or directory: 'data/sales_summary.csv'"

**Solution:** Run the data processor first to generate the CSV file:
```bash
python3 src/data_processor.py
```

#### Permission Error When Saving CSV

**Solution:** Verify that the `data/` directory exists and you have write permissions:
```bash
mkdir -p data
chmod 755 data
```

### Future Enhancements

Planned feature roadmap:

- [ ] **Multiple Data Source Support**
  - Database integration (PostgreSQL, MongoDB)
  - Read CSV, JSON, Parquet files
  - External API connections

- [ ] **Advanced Visualizations**
  - Interactive charts with Plotly/Chart.js
  - Real-time dashboard
  - Heat maps and temporal analysis

- [ ] **Machine Learning**
  - Sales forecasting
  - Anomaly detection
  - Customer segmentation

- [ ] **Distributed Processing**
  - Apache Spark integration
  - Parallel processing
  - Large volume support (>1GB)

- [ ] **REST API**
  - Data analysis endpoints
  - Authentication and authorization
  - Swagger documentation

- [ ] **Quality Improvements**
  - Structured logging
  - Robust error handling
  - Input data validation
  - Performance metrics

### GitHub Pages

The basic web interface (`web/index.html`) is configured to be served via GitHub Pages. You can access it at: `https://galafis.github.io/Big-Data-Analytics-Platform/`

#### 🎨 Web Interface Preview

![Web Dashboard](https://github.com/user-attachments/assets/6a4f287f-513d-4cd6-85f0-416f9517620b)

**Dashboard Features:**
- 📊 Real-time statistics (categories, transactions, revenue, average sales)
- 📋 Interactive table with sales data by category
- 🔄 Column sorting with one click
- 📱 Responsive design for mobile and desktop
- ⚡ Asynchronous data loading
- ❗ Error handling with user-friendly messages

### Contribution

Contributions are welcome! Please read `CONTRIBUTING.md` for more details.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

### Author

Made with ❤️ by Gabriel Demetrios Lafis.

