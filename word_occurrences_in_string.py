count_dict = {}

sentence = input("please input things: ")
sentence = sentence.split(" ")
for word in sentence:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

for sentence_word, occurrences in count_dict.items():
    print("{}: {}".format(sentence_word, occurrences))
