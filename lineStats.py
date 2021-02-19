def lineStats(inFile, outFile, threshold):
    inF = open(inFile, 'r')
    outF = open(outFile, 'w')

    for line in inF:
        count = 0
        sigCount = 0
        words = line.split()
        check = []
        for word in words:
            lword = word.lower()
            count += 1
            if len(word) > threshold and lword not in check:
                sigCount += 1
                check.append(lword)

        outF.write(" ")
        outF.write(str(count))
        outF.write(str(sigCount) + "\n")
    inF.close()
    outF.close()


print(lineStats('fish.txt', 'fishOut.txt', 3))    
