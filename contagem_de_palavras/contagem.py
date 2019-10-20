import nltk
from nltk.stem import RSLPStemmer
import Pre_processamento.ConnectionDB as ConnectionDB

#nltk.download('rslp')
#nltk.download('punkt') 

def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence

def Stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase


def contandoCoisas(texto, arquivo):

    #TTL palavraS
    p = 0
    #TTL STOPWORDS
    s = 0
    result = 0
    
    #palavraS
    palavraTxt = open(arquivo, 'r') #abri a 'base' com as palavras que estou em busca no text a ser analisado
    palavra = palavraTxt.read()
    palavraTxt.close()
    
    #STOP WORDS PERSONALIZADAS
    stoptxt = open('contagem_de_palavras/filtro.txt', 'r')
    stop = stoptxt.read()
    stoptxt.close()

    #TOKENIZANDO
    palavra = Tokenize(palavra)    
    stop = Tokenize(stop)
    texto = Tokenize(texto)
    #print(texto)
    
    #Stemmando
    palavra = Stemming(palavra)
    stop = Stemming(stop)
    texto = Stemming(texto)


    #CONTANDO COISAS EFETIVAMENTE
    for i in texto :
        if i in palavra :
            p = p+1 

    for i in texto :
        if i in stop :
            s +=1 
     
    #TOTAL DE PALAVRAS
    ttlwords = len(texto)
   
    #MENOS AS STOP WORDS
    
    if ttlwords == s:
        result = 0
    else:
        ttlwords = ttlwords - s
        result = p/ttlwords
    

    return result

def contandoCoisasPrint(texto, arquivo):
    return print(contandoCoisas(texto, arquivo))


#ok
def retornaContagem(idPessoa):
    pronome = 'contagem_de_palavras/pronomes.txt'
    absoluta = 'contagem_de_palavras/absoluta.txt'
    triste = 'contagem_de_palavras/triste.txt'
    #textoAnalisado = 'contagem_de_palavras/analisando.txt'
    #passar isso ^^ pro db depois
    segundoParse = ""
    
    pessoa = idPessoa+1
    

    mylist = ConnectionDB.obterLinhaTexto(pessoa)
    #with open(textoAnalisado, 'r') as document_text:
    #    texto = document_text.read()
    primeiroParse = mylist[0]
      #  print("primeiro parse", primeiroParse)
      
    segundoParse = primeiroParse["texto"]
    isDepre = primeiroParse["isDepressivo"]
    primeiroParse.clear()
       
    textoTratado1 = contandoCoisas(segundoParse ,pronome)
    textoTratado2 = contandoCoisas(segundoParse,absoluta)
    textoTratado3 = contandoCoisas(segundoParse,triste)

    #print(textoTratado1, textoTratado2, textoTratado3, idDepre)
    lista = criaLista(textoTratado1, textoTratado2, textoTratado3, isDepre)
    #print("Contei palavras {} vezes = nPessoas".format(pessoa))
    return lista


def retornaContagem7000(idTexto):
    pronome = 'contagem_de_palavras/pronomes.txt'
    absoluta = 'contagem_de_palavras/absoluta.txt'
    triste = 'contagem_de_palavras/triste.txt'
    #passar isso ^^ pro db depois
    
    segundoParse = ""
    
    pessoa = idTexto+1
    
    mylist = ConnectionDB.obterLinhaFrase(pessoa)
        
    primeiroParse = mylist[0]
    #print(mylist)
    #print(primeiroParse)   
          
    segundoParse = primeiroParse["texto"]
    #print(segundoParse)
    isDepre = primeiroParse["isDepressivo"]
    primeiroParse.clear()
       
    textoTratado1 = contandoCoisas(segundoParse ,pronome)
    textoTratado2 = contandoCoisas(segundoParse,absoluta)
    textoTratado3 = contandoCoisas(segundoParse,triste)

    lista = criaLista(textoTratado1, textoTratado2, textoTratado3, isDepre)
        
    return lista

def criaLista(*args):
    lista = []
    i=0
    c = len(args)

    while i < c:
               
        lista.insert(i, args[i])
        i+=1
      
    return lista