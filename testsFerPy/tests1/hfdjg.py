from nltk import FreqDist
from nltk.corpus import brown

freqs = FreqDist(brown.words())

for word, freq in freqs.items():
    print(word, freq)