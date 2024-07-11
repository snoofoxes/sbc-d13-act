prefix = ['un','re']
suffix = ['ful', 'less']
sent = input("Enter a sentence: ")

def sen_token():
    words = []
    current_word = ''
    for char in sent:
        if char in prefix:
            if current_word:
                words.append(current_word.strip()) 
            words.append(char)
            current_word = ''
        else:
            current_word += char
    if current_word:
        words.append(current_word.strip())
    
    return words


words = sen_token()
print(words)