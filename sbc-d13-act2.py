text = []
word = input("Enter a word: ")
def char_token():
    for i in word:
        text.append(i)
    print(text)
char_token()