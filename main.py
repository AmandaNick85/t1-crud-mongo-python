import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
from crud import create_user, read_users, update_user, delete_user

load_dotenv()

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
cluster_url = "cluster0.cbpyk5k.mongodb.net"
connection_string = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Criar usuário")
        print("2. Ler usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Nome do usuário: ")
            email = input("Email do usuário: ")
            create_user(client, {"name": name, "email": email})

        elif choice == '2':
            print("Usuários na coleção:")
            read_users(client)

        elif choice == '3':
            user_id = input("ID do usuário a ser atualizado: ")
            updated_name = input("Novo nome: ")
            updated_email = input("Novo email: ")
            update_user(client, ObjectId(user_id), {"name": updated_name, "email": updated_email})

        elif choice == '4':
            user_id = input("ID do usuário a ser deletado: ")
            delete_user(client, ObjectId(user_id))

        elif choice == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()

