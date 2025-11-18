from crud.crud_laureates import get_all_laureates

def test_get_all_function():
    """Testa a função get_all_laureates()"""
    print("=== TESTANDO get_all_laureates() ===")
    
    try:
        laureates = get_all_laureates()
        print(f"✅ Resultado: {type(laureates)}")
        print(f"✅ Quantidade: {len(laureates)}")

        if laureates:
            print(f"\n📋 Lista de Laureados:")
            for i, laureate in enumerate(laureates, 1):
                print(f"{i}. ID: {laureate.id} | {laureate.firstname} {laureate.lastname} | "
                      f"Gênero: {laureate.gender} | Cidade: {laureate.born_city}")
        else:
            print("ℹ️  Nenhum laureado encontrado no banco de dados.")
            
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar get_all_laureates(): {e}")
        return False

if __name__ == "__main__":
    test_get_all_function()