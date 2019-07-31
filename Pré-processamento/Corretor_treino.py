from spell_corrector_pt import SpellCorrector
import requests
import os

print('Loading dictionary')
file = open('C:/Users/felip/Desktop/Faculdade/TCC/Palavras-pt.txt','r')
r = file.read()
print('Dictionary loaded successfully')


dictionary = r.lower().split("\n")
spell = SpellCorrector(dictionary)
print('Start training (it may take a while)')
spell.train()
print('Traning successfull')


if os.path.isdir('dictionary') == False:
    os.makedirs('dictionary')

print('Saving the model...')
spell.dump_model('dictionary')
file.close()
print('Finished :D')
