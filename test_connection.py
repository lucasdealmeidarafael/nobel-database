from db.database import get_session
from models.models import Laureate

def test_connection():
    print("=== Testando Conexão com Banco ===")
    
    session = get_session()
    try:
        # Testar contagem atual
        count = session.query(Laureate).count()
        print(f"✅ Conexão OK! Total de laureados no banco: {count}")
        
        # Listar todos os laureados
        laureates = session.query(Laureate).all()
        print("Laureados existentes:")
        for laureate in laureates:
            print(f"  ID: {laureate.id}, Nome: {laureate.firstname} {laureate.lastname}")
            
        return True
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        return False
    finally:
        session.close()

if __name__ == "__main__":
    test_connection()