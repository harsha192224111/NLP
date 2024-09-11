import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

s="raining hanging Running and played are both verb forms of the word run and play."
tokens=word_tokenize(s)
print(tokens)
stem=[]
model=PorterStemmer()
for t in tokens:
    stem.append(model.stem(t))

print(stem)