import nltk
from nltk import pos_tag, word_tokenize

sentence = "The quick brown fox jumps over the lazy dog."

words=word_tokenize(sentence)
print(words)

tags=pos_tag(words)
print(tags)

nouns=[]

for word,pos in tags:
    if pos.startswith("NN"):
        nouns.append(word)

print(nouns)
if nouns:
    for noun in nouns:
        if noun[-1].lower() in {'s','x','z'} or noun[-2:].lower() in {'ch','sh'}:
            print(noun+'es')
        else:
            print(noun+'s')
else:
    print("no nouns found")