'''
O endereçamento direto é eficiente quando temos um U universo de chaves que tem um tamanho relativamente pequeno.
Em uma aplicação com conjunto dinâmico na qual cada elemento tem uma chave definida por U = {0,1,...,m-1}
Onde m não é muito grande e não há dois ou mais valores com a mesma chave.

Para representar o conjunto dinâmico usaos um array ou uma TABELA DE ENDEREÇAMENTO DIRETO:
    T[0.. m-1]
Na qual cada posição corresponde a uma chave k, se o conjunto não tem nenhum T[k], logo não existe.
A implementação é trivial:

DIRECT-ADDRESS-BUSCA(T,k)
    return T[k]

DIRECT-ADDRESS-INSERIR(T,x)
    T[chave[x]] <- x

DIRECT-ADDRESS-DELETAR(T,x)
    T[chave[x]] <- NULL

'''