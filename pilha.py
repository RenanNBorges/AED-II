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
 - isEmpty (Verifica se a pilha est[a vazia)

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

class StackConPhy:
    def __init__(self,size):
        '''Construtor da Pilha de Contiguidade Fisica
        Atrbutos:
            + limite - Limite da pilha
            + Vetor - Array com os possiveis indices da pilha
            + Base - Indice que inicia a pilha
            + Topo - Indice que representa o topo
        '''
        self.lim = size - 1
        self.vector = [None] * size
        self.base = 0
        self.top = self.base - 1

    def isEmpty(self):
        ''' Method to check if stack is empty or not, return a bool'''
        if self.top < 0:
            return True
        else:
            return False

    def push(self,data):
        ''' Method to add a new data to top of stack, return a bool about te success of method'''
        if not(self.isEmpty()):
            self.top = self.top + 1
            self.vector[self.top] = data
            return True
        else:
            return False
