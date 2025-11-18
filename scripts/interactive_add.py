from crud.crud_laureates import create_laureate
from datetime import date

def interactive_add():
    print("=== Adicionar Novo Laureado ===")

    firstname = input("Primeiro nome: ").strip()
    lastname = input("Sobrenome: ").strip()
    gender = input("Gênero (male/female): ").strip().lower()
    born_city = input("Cidade de nascimento: ").strip()
    died_country = input("País de falecimento: ").strip()

    # Data de nascimento
    print("Data de nascimento:")
    try:
        born_year = int(input("Ano: "))
        born_month = int(input("Mês: "))
        born_day = int(input("Dia: "))
        born_date = date(born_year, born_month, born_day)
    except ValueError:
        print("❌ Data inválida! Use números para ano, mês e dia.")
        return False

    # Data de morte (pode ser vazia)
    death_date = None
    has_death = input("Já faleceu? (s/n): ").strip().lower()
    if has_death == 's':
        print("Data de falecimento:")
        try:
            death_year = int(input("Ano: "))
            death_month = int(input("Mês: "))
            death_day = int(input("Dia: "))
            death_date = date(death_year, death_month, death_day)
        except ValueError:
            print("❌ Data inválida! Use números para ano, mês e dia.")
            return False

    # Confirmando
    print(f"\nResumo:")
    print(f"Nome: {firstname} {lastname}")
    print(f"Gênero: {gender}")
    print(f"Cidade natal: {born_city}")
    print(f"País de falecimento: {died_country}")
    print(f"Nascimento: {born_date}")
    if death_date:
        print(f"Falecimento: {death_date}")

    confirm = input("\nConfirmar inserção? (s/n): ").strip().lower()

    if confirm == 's':
        print("⏳ Tentando criar laureado...")
        try:
            result = create_laureate(
                firstname=firstname,
                lastname=lastname,
                gender=gender,
                born_city=born_city,
                died_country=died_country,
                born_date=born_date,
                death_date=death_date
            )
            if result:
                print(f"✅ Laureado adicionado com sucesso! ID: {result.id}")
                return True
            else:
                print("❌ A função create_laureate retornou None")
                return False
        except Exception as e:
            print(f"❌ Erro durante a criação: {e}")
            return False
    else:
        print("Operação cancelada.")
        return False

if __name__ == "__main__":
    success_count = 0
    attempt_count = 0

    while True:
        attempt_count += 1
        print(f"\n--- Tentativa {attempt_count} ---")
        if interactive_add():
            success_count += 1

        again = input("\nDeseja adicionar outro laureado? (s/n): ").strip().lower()
        if again != 's':
            break

    print(f"\nResumo: {success_count} de {attempt_count} tentativas bem-sucedidas.")