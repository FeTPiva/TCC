from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
import Pre_processamento.ConnectionDB as ConnectionDB

def exibir_resultado(valor):
    resultado = valor
    resultado = 1 if resultado[0] == '1' else 0
    return resultado


def analisar_frase(classificador, vetorizador, frase):
    return frase, classificador.predict(vetorizador.transform([frase]))

def obter_dados_das_fontes():
    diretorio_base = "contagem_de_palavras/dbs/"

    with open(diretorio_base + "imdb_labelled.txt", "r") as arquivo_texto:
        dados = arquivo_texto.read().split('\n')
         
    with open(diretorio_base + "amazon_cells_labelled.txt", "r") as arquivo_texto:
        dados += arquivo_texto.read().split('\n')

    with open(diretorio_base + "yelp_labelled.txt", "r") as arquivo_texto:
        dados += arquivo_texto.read().split('\n')

    return dados

def tratamento_dos_dados(dados):
    dados_tratados = []
    for dado in dados:
        if len(dado.split("\t")) == 2 and dado.split("\t")[1] != "":
            dados_tratados.append(dado.split("\t"))

    return dados_tratados

def dividir_dados_para_treino_e_validacao(dados):
    quantidade_total = len(dados)
    percentual_para_treino = 0.75
    treino = []
    validacao = []

    for indice in range(0, quantidade_total):
        if indice < quantidade_total * percentual_para_treino:
            treino.append(dados[indice])
        else:
            validacao.append(dados[indice])

    return treino, validacao

def pre_processamento():
    dados = obter_dados_das_fontes()
    dados_tratados = tratamento_dos_dados(dados)

    return dividir_dados_para_treino_e_validacao(dados_tratados)


def realizar_treinamento(registros_de_treino, vetorizador):
    treino_comentarios = [registro_treino[0] for registro_treino in registros_de_treino]
    treino_respostas = [registro_treino[1] for registro_treino in registros_de_treino]

    treino_comentarios = vetorizador.fit_transform(treino_comentarios)

    return BernoulliNB().fit(treino_comentarios, treino_respostas)

def realizar_avaliacao_simples(registros_para_avaliacao):
    avaliacao_comentarios = [registro_avaliacao[0] for registro_avaliacao in registros_para_avaliacao]
    avaliacao_respostas   = [registro_avaliacao[1] for registro_avaliacao in registros_para_avaliacao]

    total = len(avaliacao_comentarios)
    acertos = 0
    for indice in range(0, total):
        resultado_analise = analisar_frase(classificador, vetorizador, avaliacao_comentarios[indice])
        frase, resultado = resultado_analise
        acertos += 1 if resultado[0] == avaliacao_respostas[indice] else 0

    return acertos * 100 / total

def realizar_avaliacao_completa(registros_para_avaliacao):
    avaliacao_comentarios = [registro_avaliacao[0] for registro_avaliacao in registros_para_avaliacao]
    avaliacao_respostas   = [registro_avaliacao[1] for registro_avaliacao in registros_para_avaliacao]

    total = len(avaliacao_comentarios)
    verdadeiros_positivos = 0
    verdadeiros_negativos = 0
    falsos_positivos = 0
    falsos_negativos = 0

    for indice in range(0, total):
        resultado_analise = analisar_frase(classificador, vetorizador, avaliacao_comentarios[indice])
        frase, resultado = resultado_analise
        if resultado[0] == '0':
            verdadeiros_negativos += 1 if avaliacao_respostas[indice] == '0' else 0
            falsos_negativos += 1 if avaliacao_respostas[indice] != '0' else 0
        else:
            verdadeiros_positivos += 1 if avaliacao_respostas[indice] == '1' else 0
            falsos_positivos += 1 if avaliacao_respostas[indice] != '1' else 0

    return ( verdadeiros_positivos * 100 / total, 
             verdadeiros_negativos * 100 / total,
             falsos_positivos * 100 / total,
             falsos_negativos * 100 / total
           )


#minhas funcs personalizadas


def retorna_analisar_frase(classificador, vetorizador, frase):
    a = classificador.predict(vetorizador.transform([frase]))
    return a[0]



def retorna_Votacao_3Emocoes(idPessoa): 
    pessoa = idPessoa+1
    #print("estou na pessoa", pessoa)
    mylist = ConnectionDB.retornaNTextosGeral(pessoa)
    
    result = 0
                           
    i=0
    nTextos = ConnectionDB.nmrTextosPorPessoa(pessoa)
    #print("nTextos da pessoa",nTextos)
    #print(mylist)
    
    while i < nTextos:
        #print("to na iteração do while: ",i)
        
        primeiroParse = mylist[i]
      #  print("primeiro parse", primeiroParse)
        
        segundoParse = primeiroParse["texto"]
        primeiroParse.clear()
          
        result = result + exibir_resultado( analisar_frase(classificador, vetorizador,segundoParse))

        i+=1  

    mylist.clear()
                 
    return result    

registros_de_treino, registros_para_avaliacao = pre_processamento()
vetorizador = CountVectorizer(binary = 'true')
classificador = realizar_treinamento(registros_de_treino, vetorizador)




#b = retorna_analisar_frase(classificador, vetorizador,"so bad")
#print(b)