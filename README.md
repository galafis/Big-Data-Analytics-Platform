# Big Data Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-orange.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-blue.svg)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Big Data Analytics Platform Hero Image](https://via.placeholder.com/1200x400.png?text=Big+Data+Analytics+Platform+-+Professional+Hero+Image+Placeholder)

\n*Nota: Uma imagem hero profissional será adicionada em breve para aprimorar a apresentação visual do projeto.*

## 🇧🇷 Português

### Visão Geral

Este repositório apresenta uma **Plataforma de Análise de Big Data** em estágio inicial, focada na demonstração de processamento e análise de grandes volumes de dados. O objetivo é fornecer uma base funcional para explorar conceitos de Big Data, desde a ingestão simulada de dados até a geração de *insights* através de análises. O projeto é modular e extensível, permitindo a integração de diversas fontes de dados e ferramentas de visualização.

### Funcionalidades

-   **Geração de Dados Dummy:** Simula a criação de grandes conjuntos de dados transacionais.
-   **Processamento e Análise:** Realiza análises básicas de vendas por categoria, calculando somas, médias e contagens.
-   **Estrutura Modular:** Organização clara do código e dos dados para facilitar a compreensão e expansão.

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
├── data/                    # Armazena dados processados e resultados de análises
│   └── sales_summary.csv    # Exemplo de resultado de análise
├── src/                     # Código fonte principal
│   ├── data_processor.py    # Script para geração e análise de dados
│   └── test_data_processor.py # Testes unitários para o processador de dados
├── web/                     # Arquivos da interface web (GitHub Pages)
│   ├── index.html           # Página principal da plataforma
│   └── styles.css           # Estilos CSS para a página web
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

### GitHub Pages

A interface web básica (`web/index.html`) está configurada para ser servida via GitHub Pages. Você pode acessá-la em: `https://galafis.github.io/Big-Data-Analytics-Platform/`

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
├── data/                    # Stores processed data and analysis results
│   └── sales_summary.csv    # Example of analysis result
├── src/                     # Main source code
│   ├── data_processor.py    # Script for data generation and analysis
│   └── test_data_processor.py # Unit tests for the data processor
├── web/                     # Web interface files (GitHub Pages)
│   ├── index.html           # Main platform page
│   └── styles.css           # CSS styles for the web page
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

### GitHub Pages

The basic web interface (`web/index.html`) is configured to be served via GitHub Pages. You can access it at: `https://galafis.github.io/Big-Data-Analytics-Platform/`

### Contribution

Contributions are welcome! Please read `CONTRIBUTING.md` for more details.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

### Author

Made with ❤️ by Gabriel Demetrios Lafis.

