def words_dict(sentence):
    words = sentence.split()
    result = {}
    for word in words:
        result[word] = len(word)
    return result
sentence = "sdgaf afsdgvsd esfv sdfa"
result = words_dict(sentence)
print(sentence)
print(result)