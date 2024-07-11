
sent = input("Enter a sentence: ")
punc = ['.', ',', '!', '?', ':', ';']
def sen_token(sentence):
    words = []
    current_word = ""
    for char in sentence:
        if char in punc:
            if current_word:
                words.append((current_word + char).strip()) 
                current_word = "" 
        else:
            current_word += char  
    if current_word:
        words.append(current_word.strip())

    return words

words = sen_token(sent)
print(words)