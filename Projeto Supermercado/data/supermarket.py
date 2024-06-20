from pymongo import MongoClient
import random
import string
import time

# Conectar ao MongoDB
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.supermercado
produtos = db.produtos


def gerar_nome_aleatorio(tamanho=10):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for _ in range(tamanho))


start_time = time.time()
for produto_id in range(100000):
    produtos.insert_one({
        'filial': 'Sumare',
        'produto_id': produto_id,
        'nome': gerar_nome_aleatorio(),
        'quantidade': random.randint(1, 100),
        'preco': round(random.uniform(1, 1000), 2),
        'categoria': random.choice(['Alimentos', 'Bebidas', 'Limpeza', 'Higiene', 'Eletrônicos']),
        'ultima_atualizacao': '2024-05-31'
    })
print("Tempo de adição de nova filial: %s segundos" % (time.time() - start_time))

# # Inserir dados simulados
# for filial in ['Cidade1', 'Cidade2', 'Cidade3', 'Cidade4', 'Cidade5', 'Cidade6', 'Cidade7', 'Cidade8', 'Cidade9', 'Cidade10']:
#     for produto_id in range(100000):
#         nome = gerar_nome_aleatorio()
#         quantidade = random.randint(1, 100)
#         preco = round(random.uniform(1, 1000), 2)
#         categoria = random.choice(['Alimentos', 'Bebidas', 'Limpeza', 'Higiene', 'Eletrônicos'])
#         ultima_atualizacao = '2023-01-01'
#         produtos.insert_one({
#             'filial': filial,
#             'produto_id': produto_id,
#             'nome': nome,
#             'quantidade': quantidade,
#             'preco': preco,
#             'categoria': categoria,
#             'ultima_atualizacao': ultima_atualizacao
#         })

