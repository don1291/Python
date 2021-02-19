def lookInto(inFile, outFile, searchString):
    inF = open(inFile, 'r')
    outF = open(outFile, 'w')
    for line in inF:
        instances = line.count(searchString):
        outF.write(str(instances))
    inF.close()
    outF.close()
print(lookInto('lewis.txt', 'out.txt', 'the'))
