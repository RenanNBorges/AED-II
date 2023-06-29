'''
Feito por Renan Nunes Borges
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
 - isEmpty (Verifica se a pilha est[a vazia)

--------------------- TIPOS ---------------------
 + CONTIGUIDADE FÍSICA:
    - Tem que definir o Limite e a Base da pilha
    - É colocado em um vetor que só tem acesso ao índice do topo

 + ENCADEADA:
    - Usa um descritor para armazenar o nodo do Topo da pilha
    - Usa nodos para indicar o topo da pilha
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackLinked:
    def __init__(self):
        self.__top = None

    def isEmpty(self):
        if self.__top != None:
            return False
        else:
            return True

    def push(self,data):
        new_top = Node(data)