sentence = input("The sentence: ")
sen2 = ""
for i in range(len(sentence)):
    if (sentence[i] == '<'):
        while (sentence[i + 1] != '>'):
            i = i + 1
            sen2 += sentence[i]
        print(sen2)
        sen2 = ""
