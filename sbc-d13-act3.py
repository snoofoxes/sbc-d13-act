prefix = ['un', 're']
suffix = ['ful', 'less']

text = input("Enter a text: ")

def sub_token():
    word = []
    temp = []
    i = 0
    
    while i < len(text):
        temp.append(text[i])
        t = ''.join(temp)
        
        if t in prefix or t in suffix:
            word.append(t)
            temp = []
        else:
            i += 1
            continue
    
        i += 1
    
    if temp:
        word.append(''.join(temp))
    
    return word

words = sub_token()
print(words)