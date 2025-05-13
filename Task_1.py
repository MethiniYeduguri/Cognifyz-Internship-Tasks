#string reversal function
def string_reversal(text):
    duplicate_text=""
    for i in range(-1,-(len(text)+1),-1):
        duplicate_text+=text[i]
    return duplicate_text

#input for string reversal
word=input("Enter a word or sentence=")
output=string_reversal(word)

#print the result
print(output)
