import sys
import os

# Adiciona o diretório raiz ao path para imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crud.crud_laureates import get_laureate_by_id, delete_laureate, get_all_laureates

def interactive_delete():
    print("=== DELETAR LAUREADO ===")

    # Lista laureados
    laureates = get_all_laureates()
    if not laureates:
        print("Nenhum laureado encontrado.")
        return False
    
    print(f"\n--- LAUREADOS DISPONÍVEIS ({len(laureates)} total) ---")
    for laureate in laureates:
        print(f"ID: {laureate.id} | {laureate.firstname} {laureate.lastname} | Gênero: {laureate.gender}")

    try:
        laureate_id = int(input("\nDigite o ID do laureado a ser DELETADO: "))
    except ValueError:
        print("❌ ID inválido!")
        return False
    
    # Procura e mostra laureado
    laureate = get_laureate_by_id(laureate_id)
    if not laureate:
        print(f"❌ Laureado com ID {laureate_id} não encontrado.")
        return False
    
    print(f"\n⚠️  ATENÇÃO: Você está prestes a DELETAR:")
    print(f"    Nome: {laureate.firstname} {laureate.lastname}")
    print(f"    Gênero: {laureate.gender}")
    print(f"    Cidade natal: {laureate.born_city}")
    print(f"    ID: {laureate.id}")

    confirm = input("\n❌ TEM CERTEZA que deseja deletar? (digite 'DELETAR' para confirmar): ").strip()

    if confirm == 'DELETAR':
        result = delete_laureate(laureate_id)
        if result:
            print("✅ Laureado deletado com sucesso!")
        else:
            print("❌ Falha ao deletar laureado.")
        return result
    else:
        print("❌ Deleção cancelada.")
        return False

if __name__ == "__main__":
    interactive_delete()