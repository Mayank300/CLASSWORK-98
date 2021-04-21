def countWordsFromFile():
    fileName = input("Enter the file name: ")
    file = open(fileName, 'r')
    num_words = 0
    for line in file:
        words = line.split()
        num_words = num_words + len(words)

    print(num_words)


countWordsFromFile()
