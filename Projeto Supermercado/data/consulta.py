import time

start_time = time.time()
produtos.find_one({'filial': 'Cidade3', 'produto_id': 12345})
print("Tempo de consulta: %s segundos" % (time.time() - start_time))