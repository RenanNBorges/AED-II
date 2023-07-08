
from tabela import Table
def hash(key,size):
    return key % (size + 1)


registro = Table(8)
registro.insert(73, 'João')
registro.insert(44, 'Carlos')
registro.insert(37, 'Carlos')
registro.insert(30, 'Marcia')
registro.insert(59, 'Ronaldo')
registro.insert(61, 'Michel')
registro.insert(99, 'Carlos')

