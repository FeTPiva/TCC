import nltk


textoAnalisado = 'analisando.txt'

with open(textoAnalisado, 'r') as document_text:
    minhaString = document_text.read()

stemmer = nltk.stem.RSLPStemmer()

print(stemmer.stem('amor amoroso absolutamente absoluto'))