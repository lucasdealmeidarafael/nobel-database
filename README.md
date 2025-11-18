# 🏆 Nobel Prize Database Management

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-green)

Sistema completo de gerenciamento de laureados do Prêmio Nobel desenvolvido em Python com PostgreSQL e SQLAlchemy.

## ✨ Funcionalidades

- ✅ **Adicionar** novos laureados
- ✅ **Listar** todos os laureados cadastrados  
- ✅ **Estatísticas** do banco de dados
- ✅ **Atualizar** informações de laureados existentes
- ✅ **Deletar** laureados do sistema

## 🛠️ Tecnologias

- **Python 3.8+** - Linguagem principal
- **PostgreSQL** - Banco de dados relacional
- **SQLAlchemy** - ORM para mapeamento objeto-relacional
- **Psycopg2** - Driver PostgreSQL para Python

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- PostgreSQL instalado e rodando

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/lucasdealmeidarafael/nobel-database.git
   cd nobel-database

## 🧪 Testes

Scripts de teste incluídos para verificar funcionalidades:

```bash
# Testar conexão com o banco
python test_connection.py

# Testar listagem de todos os laureados
python test_get_all.py