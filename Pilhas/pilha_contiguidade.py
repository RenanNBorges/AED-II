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
'''

class StaticStack:
    def __init__(self,size):
        '''Construtor da Pilha de Contiguidade Fisica
        Atrbutos:
            + limite - Limite da pilha
            + Vetor - Array com os possiveis indices da pilha
            + Base - Indice que inicia a pilha
            + Topo - Indice que representa o topo
        '''
        self.__lim = size - 1
        self.__vector = [None] * size
        self.__base = 0
        self.__top = self.__base - 1

    def isEmpty(self):
        ''' Method to check if stack is empty or not, return a bool'''
        if self.__top < 0:
            return True
        else:
            return False

    def push(self,data):
        ''' Method to add a new data to top of stack, return a bool about te success of method'''
        if self.__top < self.__lim:
            self.__top = self.__top + 1
            self.__vector[self.__top] = data
            return True
        else:
            print('Stack OverFlow')
            return False

    def peek(self):
        ''' Method to return top of stack, if is empty return a None'''
        if self.isEmpty():
            return None
        else:
            return self.__vector[self.__top]

    def pop(self):
        ''' Method to remove a element in stack, return a bool'''
        if self.__top >= self.__base:
            self.__top = self.__top - 1
            return True
        else:
            print('Stack UnderFlow')
            return False

    def destroy(self):
        if not(self.isEmpty()):
            self.__top = self.__base - 1
            return True
        else:
            return False

if __name__ == "__main__":
    test_static_stack = StaticStack(10)
    print(test_static_stack.isEmpty())
    test_static_stack.push(1)
    print(test_static_stack.peek())
    test_static_stack.push(3)
    print(test_static_stack.peek())
    test_static_stack.push(4)
    print(test_static_stack.peek())
    test_static_stack.push(5)
    print(test_static_stack.peek())

    test_static_stack.pop()
    print(test_static_stack.peek())
    test_static_stack.pop()
    print(test_static_stack.peek())
    test_static_stack.pop()
    print(test_static_stack.peek())
    test_static_stack.pop()
    print(test_static_stack.peek())
    test_static_stack.push(5)
    test_static_stack.push(1)
    test_static_stack.push(4)
    test_static_stack.push(6)
    print(test_static_stack.peek())
    test_static_stack.destroy()
    print(test_static_stack.peek())



