'''
Arquivo Contendo Tipos Abstratos de Dado Pilha com principio LIFO (Last In, First Out) são Lista Lineares Especiais.

Tem acesso restrito, somente ao topo da pilha
Restrições de Operações:
 * Inserir
 * Excluir
 * Consultar

--------------------- OPERAÇÕES ---------------------
 - new (Criar nova pilha Vazia)
 - push (Inserir um nó no topo da pilha)
 - pop (Excluir o nó no topo da pilha)
 - top (COnsulta o nó no topo da pilha)
 - destroy (Destrói a pilha)

--------------------- TIPOS ---------------------
 + CONTIGUIDADE FÍSICA:
    - Tem que definir o Limite e a Base da pilha
    - É colocado em um vetor que só tem acesso ao índice do topo

 + ENCADEADA:
    - Usa um descritor para armazenar o nodo do Topo da pilha
'''

class Nodo:
    def __init__(self,data):
        self.data = data
        self.next = None
