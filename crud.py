from pymongo import MongoClient, errors

def create_user(client, user_data):
    try:
        users = client["lidb"]["users"]
        result = users.insert_one(user_data)
        print(f"Usuário criado com ID: {result.inserted_id}")
    except errors.PyMongoError as e:
        print(f"Erro ao criar usuário: {e}")

def read_users(client):
    try:
        users = client["lidb"]["users"]
        for user in users.find():
            print(user)
    except errors.PyMongoError as e:
        print(f"Erro ao ler usuários: {e}")

def update_user(client, user_id, updated_data):
    try:
        users = client["lidb"]["users"]
        result = users.update_one({"_id": user_id}, {"$set": updated_data})
        if result.modified_count > 0:
            print(f"Usuários atualizados: {result.modified_count}")
        else:
            print("Nenhum usuário foi atualizado.")
    except errors.PyMongoError as e:
        print(f"Erro ao atualizar usuário: {e}")

def delete_user(client, user_id):
    try:
        users = client["lidb"]["users"]
        result = users.delete_one({"_id": user_id})
        if result.deleted_count > 0:
            print(f"Usuário com ID: {user_id} deletado")
        else:
            print("Nenhum usuário foi deletado.")
    except errors.PyMongoError as e:
        print(f"Erro ao deletar usuário: {e}")