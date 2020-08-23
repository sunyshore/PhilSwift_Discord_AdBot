
file = open("negativeWord", "r")
negativeWord = [];
for word in file:
    negativeWord.append(word[0:-1])
print(negativeWord)