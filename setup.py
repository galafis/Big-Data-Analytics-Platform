#!/usr/bin/env python3
"""
Setup script for Big Data Analytics Platform
Automates the installation and initial configuration process
"""

import sys
import subprocess
import os
from pathlib import Path

def print_header(message):
    """Print formatted header message."""
    print("\n" + "="*60)
    print(f"  {message}")
    print("="*60 + "\n")

def check_python_version():
    """Check if Python version is 3.7 or higher."""
    print_header("🐍 Verificando versão do Python")
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Erro: Python 3.7 ou superior é necessário")
        return False
    
    print("✅ Versão do Python adequada")
    return True

def install_dependencies():
    """Install required Python packages."""
    print_header("📦 Instalando dependências")
    
    try:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
        ])
        print("✅ Dependências instaladas com sucesso")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def create_directories():
    """Create necessary directories."""
    print_header("📁 Criando diretórios necessários")
    
    directories = ['data', 'logs']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Diretório '{directory}' criado/verificado")
    
    return True

def run_tests():
    """Run unit tests to verify installation."""
    print_header("🧪 Executando testes")
    
    try:
        result = subprocess.run([
            sys.executable, 'src/test_data_processor.py'
        ], capture_output=True, text=True)
        
        print(result.stdout)
        
        if result.returncode == 0:
            print("✅ Todos os testes passaram")
            return True
        else:
            print("❌ Alguns testes falharam")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Erro ao executar testes: {e}")
        return False

def run_initial_data_generation():
    """Generate initial sample data."""
    print_header("🔄 Gerando dados iniciais")
    
    try:
        result = subprocess.run([
            sys.executable, 'src/data_processor.py'
        ], capture_output=True, text=True)
        
        print(result.stdout)
        
        if result.returncode == 0:
            print("✅ Dados iniciais gerados com sucesso")
            return True
        else:
            print("❌ Erro ao gerar dados iniciais")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def print_success_message():
    """Print success message with next steps."""
    print_header("🎉 Instalação Concluída com Sucesso!")
    
    print("Próximos passos:\n")
    print("1. Para gerar novos dados, execute:")
    print("   python3 src/data_processor.py\n")
    print("2. Para executar testes:")
    print("   python3 src/test_data_processor.py\n")
    print("3. Para visualizar o dashboard web:")
    print("   Abra web/index.html em seu navegador\n")
    print("4. Para mais informações, consulte README.md\n")
    print("="*60 + "\n")

def main():
    """Main setup function."""
    print("\n" + "="*60)
    print("  BIG DATA ANALYTICS PLATFORM - SETUP")
    print("="*60)
    
    # Change to script directory
    os.chdir(Path(__file__).parent)
    
    # Run setup steps
    steps = [
        ("Verificando Python", check_python_version),
        ("Instalando dependências", install_dependencies),
        ("Criando diretórios", create_directories),
        ("Executando testes", run_tests),
        ("Gerando dados iniciais", run_initial_data_generation)
    ]
    
    for step_name, step_func in steps:
        if not step_func():
            print(f"\n❌ Falha na etapa: {step_name}")
            print("Por favor, corrija os erros e execute o setup novamente.")
            return 1
    
    print_success_message()
    return 0

if __name__ == "__main__":
    sys.exit(main())
