import glob
from textblob import TextBlob
import numpy as np


def mergefiles():
    male = []
    female = []
    malelines = []
    femalelines = []

    for filename in glob.glob('datafiles/*.txt'):
        if 'female' in filename.lower() or 'she' in filename.lower() or 'women' in filename.lower() or 'femalecharacter' in filename.lower() or 'woman' in filename.lower():
            female.append(filename)
        else:
            male.append(filename)

    for i in range(len(male)):
        with open(male[i]) as file:  # Use file to refer to the file object
            lines = [(line) for line in (file)]
            if len(lines) == 1:
                pass
            else:
                malelines.extend(lines)

    for i, item in enumerate(malelines):
        if item[0] != 'H':
            malelines[i] = "He's " + item

    for i in range(len(female)):
        with open(female[i]) as file:
            lines = [(line) for line in (file)]
            if len(lines) == 1:
                pass
            else:
                femalelines.extend(lines)

    for i, item in enumerate(femalelines):
        if item[0] == 'A':
            femalelines[i] = "She's " + item

    Lines = malelines + femalelines
    return Lines, malelines, femalelines


def sentimentalayisis(malelines, femalelines):
    male = []
    female = []
    for item in malelines:
        male.append(TextBlob(item).sentiment[0])

    for item in femalelines:
        female.append(TextBlob(item).sentiment[0])

    Best = Lines[np.argmax(male)] + LinesF[np.argmax(female)]
    Worst = Lines[np.argmin(male)] + LinesF[np.argmin(female)] + 'They fight crime!'
    return Best, Worst


def descriptions(Lines):
    adj = []
    for i in range(len(Lines)):
        adj.extend(Lines[i].strip(' ').split(' ')[2:4])
    ADJ = ' '.join(adj)

    common = {}
    for item in ADJ.split(' '):
        if item in common:
            common[item] += 1
        else:
            common[item] = 1
    topn = sorted(common.items(), key=lambda x: x[1], reverse=True)
    for i in range(10):
        print(topn[i][0], topn[i][1])
    return topn


if __name__ == "__main__":
    Lines, malelines, femalelines = mergefiles()
    Best, Worst = sentimentalayisis(malelines, femalelines)
    topn = descriptions(Lines)
    for i in range(10):
        print(topn[i])