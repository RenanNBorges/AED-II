"""
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
 - top (Consulta o nó no topo da pilha)
 - destroy (Destrói a pilha)
 - isEmpty (Verifica se a pilha est[a vazia)

--------------------- TIPOS ---------------------
 + CONTIGUIDADE FÍSICA:
    - Tem que definir o Limite e a Base da pilha
    - É colocado em um vetor que só tem acesso ao índice do topo

 + ENCADEADA:
    - Usa um descritor para armazenar o nodo do Topo da pilha
    - Usa nodos para indicar o topo da pilha
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> {self.next}'

    def __repr__(self):
        return f'{self.data} -> {self.next}'


class DynamicStack:
    def __init__(self):
        self.__top = None

    def __repr__(self):
        return f'{self.__top}'

    def is_empty(self):
        if self.__top is not None:
            return False
        else:
            return True

    def peek(self):
        if not(self.is_empty()):
            return self.__top.data
        else:
            return None

    def push(self,data):
        new_top = Node(data)
        if not(self.is_empty()):
            new_top.next = self.__top
        self.__top = new_top

    def pop(self):
        if self.is_empty():
            return False
        else:
            self.__top = self.__top.next
            return True

    def destroy(self):
        while not(self.is_empty()):
            self.pop()



if __name__ == "__main__":
    stack_test = DynamicStack()

    stack_test.peek()
    stack_test.push(2)
    stack_test.peek()
    stack_test.push(1)
    stack_test.peek()
    stack_test.push(7)
    stack_test.peek()
    stack_test.push(8)
    stack_test.pop()
    stack_test.peek()
    stack_test.pop()
    stack_test.peek()
    stack_test.destroy()
    stack_test.peek()





