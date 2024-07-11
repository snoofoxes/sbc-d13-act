punc = ['.', ',', '"','[]','!','?',':',';']
sent = input("Enter a sentence: ")
words = []
def sen_token():
    sep = ''
    for i in sent:
        if i in punc:
            words.append(sep)
            sep = ''
        else:
            sep += i
    if sep:
        words.append(sep)

sen_token()
print(words)