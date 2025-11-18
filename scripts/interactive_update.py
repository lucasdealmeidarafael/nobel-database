from crud.crud_laureates import get_laureate_by_id, update_laureate, get_all_laureates
from datetime import date

def list_laureates_for_selection():
    """Lista laureados para seleção."""
    laureates = get_all_laureates()
    print(f"\n--- LAUREADOS DISPONÍVEIS ({len(laureates)} total) ---")
    for laureate in laureates:
        print(f"ID: {laureate.id} | {laureate.firstname} {laureate.lastname} | Gênero: {laureate.gender} | Cidade: {laureate.born_city}")
    return laureates

def interactive_update():
    print("=== ATUALIZAR LAUREADO EXISTENTE ===")

    # Lista laureados
    laureates = list_laureates_for_selection()

    if not laureates:
        print("Nenhum laureado encontrado para atualizar.")
        return None
    
    try:
        laureate_id = int(input("\nDigite o ID do laureado a ser atualizado: "))
    except ValueError:
        print("❌ ID inválido!")
        return None
    
    # Procura laureado
    laureate = get_laureate_by_id(laureate_id)
    if not laureate:
        print(f"❌ Laureado com ID {laureate_id} não encontrado.")
        return None
    
    print(f"\nAtualizando: {laureate.firstname} {laureate.lastname}")
    print("Deixe em branco para manter o valor atual.\n")

    # Coleta os dados
    firstname = input(f"Primeiro nome [{laureate.firstname}]: ").strip()
    lastname = input(f"Sobrenome [{laureate.lastname}]: ").strip()
    gender = input(f"Gênero (male/female) [{laureate.gender}]: ").strip()
    born_city = input(f"Cidade de nascimento [{laureate.born_city}]: ").strip()
    died_country = input(f"País de falecimento [{laureate.died_country}]: ").strip()

    # Processamento das datas
    born_date = None
    print(f"\nData de nascimento atual: {laureate.born}")
    change_born = input("Alterar data de nascimento? (s/n): ").strip().lower()
    if change_born == 's':
        print("Nova data de nascimento:")
        try:
            born_year = int(input("Ano: "))
            born_month = int(input("Mês: "))
            born_day = int(input("Dia: "))
            born_date = date(born_year, born_month, born_day)
        except ValueError:
            print("❌ Data inválida! Use números para ano, mês e dia.")
            return None

    death_date = None
    print(f"\nData de falecimento atual: {laureate.death}")
    change_death = input("Alterar data de falecimento? (s/n): ").strip().lower()
    if change_death == 's':
        print("Nova data de falecimento:")
        try:
            death_year = int(input("Ano: "))
            death_month = int(input("Mês: "))
            death_day = int(input("Dia: "))
            death_date = date(death_year, death_month, death_day)
        except ValueError:
            print("❌ Data inválida! Use números para ano, mês e dia.")
            return None

    # Prepara dados para atualização
    update_data = {}
    if firstname: update_data['firstname'] = firstname
    if lastname: update_data['lastname'] = lastname
    if gender: update_data['gender'] = gender
    if born_city: update_data['born_city'] = born_city
    if died_country: update_data['died_country'] = died_country
    if born_date: update_data['born'] = born_date
    if death_date: update_data['death'] = death_date

    if update_data:
        # Confirma
        print(f"\nResumo das alterações:")
        for key, value in update_data.items():
            print(f"  {key}: {value}")
        
        confirm = input("\nConfirmar atualização? (s/n): ").strip().lower()
        if confirm == 's':
            result = update_laureate(laureate_id, **update_data)
            if result:
                print("✅ Atualização realizada com sucesso!")
            return result
        else:
            print("❌ Atualização cancelada.")
            return None
    else:
        print("ℹ️  Nenhuma alteração foi feita.")
        return None

if __name__ == "__main__":
    interactive_update()