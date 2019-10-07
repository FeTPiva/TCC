#logica principal processamento de sentimentos

import Pre_processamento.ConnectionDB as ConnectionDB

c = ConnectionDB.totalPessoas()
j = 0

while j < c:
    k = j+1
    mylist = ConnectionDB.retornaNTextosGeral(k)

    nTextos = ConnectionDB.nmrTextosPorPessoa(k)


    i = 0
    while i < nTextos:
        print(mylist)
        mylist.clear()
        i+=1

    j +=1