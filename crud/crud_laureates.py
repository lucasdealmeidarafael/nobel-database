from db.database import get_session
from models.models import Laureate

def create_laureate(firstname, lastname, gender, born_city, died_country, born_date, death_date):
    
    session = get_session()
    try:
        laureate = Laureate(
            firstname=firstname,
            lastname=lastname,
            gender=gender,
            born_city=born_city,
            died_country=died_country,
            born=born_date,
            death=death_date
        )
        session.add(laureate)
        session.commit()
        print(f"Laureado {firstname} {lastname} criado com sucesso!")
        return laureate
    except Exception as e:
        print(f"❌ ERRO na criação do laureado: {e}")
        import traceback
        traceback.print_exc()
        session.rollback()
        return None
    finally:
        session.close()

def get_all_laureates():
    """Retorna todos os laureados"""
    session = get_session()
    try:
        return session.query(Laureate).all()
    finally:
        session.close()

def get_laureate_by_id(laureate_id):
    """Busca um laureado pelo ID."""
    session = get_session()
    try:
        return session.query(Laureate).filter(Laureate.id == laureate_id).first()
    finally:
        session.close()

def update_laureate(laureate_id, **kwargs):
    session = get_session()
    try:
        laureate = session.query(Laureate).filter(Laureate.id == laureate_id).first()
        if not laureate:
            print(f"❌ Laureado com ID {laureate_id} não encontrado.")
            return None
        
        changes_made = False
        for key, value in kwargs.items():
            if hasattr(laureate, key) and value is not None:
                current_value = getattr(laureate, key)
                if str(current_value) != str(value):
                    print(f"DEBUG: Atualizando {key} de '{current_value}' para '{value}'")
                    setattr(laureate, key, value)
                    changes_made = True
            else:
                print(f"DEBUG: Campo {key} não existe no modelo ou valor é None")

        if changes_made:
            session.flush()
            print("DEBUG: Flush realizado sem erros")
            session.commit()
            print("DEBUG: Commit realizado")
            session.refresh(laureate)
            print(f"DEBUG: Após refresh - born_city: {laureate.born_city}")
            print(f"✅ Laureado ID {laureate_id} atualizado com sucesso!")
        else:
            print("ℹ️  Nenhuma alteração foi necessária")
        
        return laureate
        
    except Exception as e:
        session.rollback()
        print(f"❌ Erro ao atualizar laureado: {e}")
        import traceback
        traceback.print_exc()
        return None
    finally:
        session.close()

def delete_laureate(laureate_id):
    session = get_session()
    try:
        laureate = session.query(Laureate).filter(Laureate.id == laureate_id).first()
        if laureate:
            session.delete(laureate)
            session.commit()
            print(f"✅ Laureado ID {laureate_id} deletado com sucesso!")
            return True
        else:
            print(f"❌ Laureado com ID {laureate_id} não encontrado.")
            return False
    except Exception as e:
        session.rollback()
        print(f"❌ Erro ao deletar laureado: {e}")
        return False
    finally:
        session.close()