def wordLineCount(inFile):
    
    inF = open(inFile, "rt")
    dict = {}
    for line in inF:
        usedWords = []
        words = line.split()
        for word in words:
            if word not in usedWords:
                usedWords.append(word)
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
    inF.close()
    return dict
    
print(wordLineCount('ben.txt'))
