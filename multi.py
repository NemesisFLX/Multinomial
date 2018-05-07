from reader import readWord
import pandas as pd
import numpy as np

classes = 20
words = 60 # Default = 93508
columns=['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale',
         'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian',
         'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']
indizes = []
file = open("20news/20news.voc", "r", encoding="utf8")
word = ''
countIndizes = 0
while (word is not None) and countIndizes <= words:
    word = readWord(file)
    countIndizes += 1
    if word is not None and countIndizes <= words:
        indizes.append(word)


A = pd.DataFrame(np.zeros([words, classes]), columns=columns, index=indizes)


# Fill Matrix with Count entrys
file = open("20news/20news.tr", "r", encoding="utf8")
word = ''
currentColumn = ''
countLoops = 0
while word is not None:
    word = readWord(file)
    countLoops += 1
    if countLoops % 10000 == 0:
        print(countLoops)
    if word is not None:
        if word in columns:
            currentColumn = word
        elif word in indizes:
            count = int(readWord(file))
            A.at[word, currentColumn] += count

# Estimate lambdas for the different classes with max likelihood
# For faster Start:
# [5605.45, 5135.05, 4665.1, 3745.3, 3359.8, 5993.85, 2890.1, 3922.3, 3728.75, 4022.25, // Falsch
#  5158.4, 6389.8, 3760.9, 5822.5, 5999.5, 6079.75, 6123.4, 8410.3, 7219.55, 5654.6]    // Falsch
# [1.1989241562219275, 1.0983124438550713, 0.9977969799375455, 0.8010651495059247, 0.7186123112460966,
#  1.2819972622663303, 0.61815031868931, 0.8389228729092698, 0.7975253454249904, 0.8603007229327972,
#  1.1033066689481115, 1.3666852034050563, 0.80440176241605, 1.2453479916156907, 1.283205715019036, 1.3003700218163152,
#  1.3097061214013774, 1.7988407408991745, 1.5441566496984216, 1.2094366257432518]
lambdas = []
for column in columns:
    lambdas.append(A[column].sum()/words)
