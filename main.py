"""
Sistema de Gerenciamento do Nobel Prize Database
"""

from scripts.interactive_add import interactive_add
from scripts.interactive_update import interactive_update
from scripts.interactive_delete import interactive_delete
from db.database import get_session
from models.models import Laureate
from sqlalchemy import func

def show_menu():
    print("\n" + "=" * 50)
    print("       NOBEL PRIZE DATABASE MANAGEMENT")
    print("=" * 50)
    print("1. Adicionar novo laureado")
    print("2. Listar todos os laureados")
    print("3. Estatísticas do banco")
    print("4. Atualizar laureado existente")
    print("5. Deletar laureado")
    print("6. Sair")
    print("=" * 50)

def list_all_laureates():
    session = get_session()
    try:
        laureates = session.query(Laureate).all()
        print(f"\n--- LISTA DE LAUREADOS ({len(laureates)} total) ---")
        for laureate in laureates:
            print(f"ID: {laureate.id} | {laureate.firstname} {laureate.lastname} | "
                  f"Gênero: {laureate.gender} | Cidade: {laureate.born_city}")
    finally:
        session.close()

def show_statistics():
    session = get_session()
    try:
        total = session.query(Laureate).count()
        male = session.query(Laureate).filter(func.lower(Laureate.gender) == 'male').count()
        female = session.query(Laureate).filter(func.lower(Laureate.gender) == 'female').count()
        other = total - male - female

        print(f"\n--- ESTATÍSTICAS ---")
        print(f"Total de laureados: {total}")
        print(f"Laureados homens: {male}")
        print(f"Laureados mulheres: {female}")
        if other > 0:
            print(f"Outros/Desconhecidos: {other}")

        if total > 0:
            print(f"\nPorcentagens:")
            print(f"Homens: {(male/total)*100:.1f}%")
            print(f"Mulheres: {(female/total)*100:.1f}%")
            if other > 0:
                print(f"Outros: {(other/total)*100:.1f}%")

    finally:
        session.close()

def main():
    while True:
        show_menu()
        choice = input("\nEscolha uma opção (1-6): ").strip()

        if choice == '1':
            interactive_add()
        elif choice == '2':
            list_all_laureates()
        elif choice == '3':
            show_statistics()
        elif choice == '4':
            interactive_update()
        elif choice == '5':
            interactive_delete()
        elif choice == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()