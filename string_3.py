sentence_original = input("The sentence: ")
sentence_copy = ""
for i in range(len(sentence_original)):
    sentence_copy += sentence_original[(len(sentence_original)-i)-1]

print(sentence_copy)
