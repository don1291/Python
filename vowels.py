def vowelCount(inFile, outFile):
    vowels = 'aeiouAEIOU'
    inF = open(inFile, 'r')
    outF = open(outFile, 'w')
    for line in inF:
        vowelCount = 0
        for letter in line:
            if letter in vowels:
                vowelCount += 1
        outF.write(str(vowelCount)+'\n')
    inF.close()
    outF.close()
print(vowelCount('paradox.txt', 'out.txt'))
