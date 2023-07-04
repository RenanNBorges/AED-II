"""
Feito por Renan Nunes Borges

Arquivo contendo representações de Tipos Abstratos de Dados Fila

Filas usam do príncipio de FIFO (First in, First Out)
Tem acesso restrito há o primeiro e ultimo elemento que foi inserido
Mas as operações de consulta e exclusão são somente pelo primeiro
OPERAÇÕES que são afetas pelas restrições:
 * Inserir
 * Excluir
 * Consultar

--------------------- OPERAÇÕES ---------------------
• criar uma fila vazia
• inserir um nó no final da fila
• excluir o nó do início da fila
• consultar nó do início da fila
• destruir a fila

Filas encadeadas tem as seguintes propriedades:
Um descritor com o n[o de inicio e fim
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class DynamicQueue:
    def __init__(self):
        self.ini = None
        self.end = None

    def is_empty(self):
        if self.ini and self.end is None:
            return False
        else:
            return True

