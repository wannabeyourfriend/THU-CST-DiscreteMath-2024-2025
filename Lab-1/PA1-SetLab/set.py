def readAndPrintUniqueWords(filename):
    infile = open(filename, 'r')
    word_set = set()
    for line in infile:
        for word in line.split():
            if word not in word_set:
                print(word)
                word_set.add(word)
    infile.close()

def shakeSpeare(filename):
    infile = open(filename, 'r')
    word_set = set()
    result = set()
    
    for line in infile:
        for word in line.split():
            if len(word) >= 5:
                word = word.lower()
                reversed_word = word[::-1]
                
                if reversed_word in word_set:
                    result.add(word)
                    result.add(reversed_word)
                
                word_set.add(word)
    
    infile.close()
    return result