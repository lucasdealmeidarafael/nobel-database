from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import urllib.parse

# =============================================
# CONFIGURAÇÃO DO BANCO DE DADOS
# EDITE ESTAS VARIÁVEIS COM SUAS CREDENCIAIS
# =============================================

DB_USER = "seu_usuario_postgresql"        # 👈 ALTERE: Seu usuário PostgreSQL
DB_PASSWORD = "sua_senha_postgresql"      # 👈 ALTERE: Sua senha PostgreSQL  
DB_HOST = "localhost"                     # 👈 ALTERE se necessário
DB_NAME = "nobel_database"                # 👈 ALTERE se quiser outro nome

# Codificar senha para URL (caso tenha caracteres especiais)
encoded_password = urllib.parse.quote_plus(DB_PASSWORD)

# Construir URL de conexão
DATABASE_URL = f"postgresql://{DB_USER}:{encoded_password}@{DB_HOST}/{DB_NAME}"

# =============================================
# CONEXÃO COM O BANCO
# =============================================

try:
    # Criar engine
    engine = create_engine(DATABASE_URL)
    
    # Testar conexão
    with engine.connect() as conn:
        print(f"✅ Conectado ao banco '{DB_NAME}' em {DB_HOST}")
        
except Exception as e:
    print(f"❌ Erro ao conectar ao banco: {e}")
    print("\n📋 INSTRUÇÕES:")
    print("1. Configure suas credenciais no arquivo db/database.py")
    print("2. Certifique-se que o PostgreSQL está rodando")
    print("3. Crie o banco de dados executando:")
    print("   CREATE DATABASE nobel_database;")
    print("4. Verifique se o usuário e senha estão corretos")
    exit(1)

# Criar tabelas no banco
Base = declarative_base()
Base.metadata.create_all(engine)

# Criar session para interagir com o banco
Session = sessionmaker(bind=engine, expire_on_commit=False)

def get_session():
    return Session()