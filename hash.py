from tabela import Table


def hash(key, size):
    return key % (size + 1)


registro = Table(7)

registro.insert(73, 'João')
registro.insert(44, 'Carlos')
registro.insert(37, 'Carlos')
registro.insert(30, 'Marcia')
registro.insert(59, 'Ronaldo')
registro.insert(61, 'Michel')
registro.insert(99, 'Carlos')

keys = []
tabela_hash = Table(7)
for i in range(1, 8):
    hash_index = hash(registro.key[i], 7)
    tabela_hash.insert(hash_index, registro.key[i])
    print(hash_index)

# TODO Add Open addressing Linked
