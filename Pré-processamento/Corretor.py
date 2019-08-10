from spell_corrector_pt import SpellCorrector
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

spell = SpellCorrector()

def estaNoDicionario(palavra):
	file = open('Pré-processamento/Palavras-pt.txt','r', encoding="utf8")
	r = file.read()
	dictionary = r.lower().split("\n")
	for y in dictionary:
		if palavra == y:
			return True
	return False

def retornaCorrecaoGiria(palavra):
	giria_formatada=palavra
	file = open('Pré-processamento/Girias.txt','r', encoding="utf8")
	r = file.read()
	dictionary = r.lower().split("\n")
	for z in dictionary:
		palavra_correta = z.split(",")
		if palavra_correta[0] == palavra:
			giria_formatada = palavra_correta[1]
	return giria_formatada


def correct_phrase(frase):
	frase_tokens_correta = []
	spell.load_model('dictionary')
	frase = frase.lower()
	frase_tokens = nltk.word_tokenize(frase)
	for x in frase_tokens:
		x_correto = spell.get_correct_word(x)
		if estaNoDicionario(x):
			x_correto = x
		else:
			x_correto = retornaCorrecaoGiria(x)
		frase_tokens_correta.append(x_correto)
	frase_tokens_correta = TreebankWordDetokenizer().detokenize(frase_tokens_correta)
	return frase_tokens_correta

