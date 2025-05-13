#function to check a word is palindrome
def is_palindrome(word):
    length=len(word)
    times=length//2
    i=0
    j=length-1
    for n in range(times):
        if(not(word[i]==word[j])):
            return False
        i+=1
        j-=1
    return True

#input
word=input("Enter a word=")
lowcase=word.lower()

#output
if(is_palindrome(lowcase)):
    print("It's a palindrome")
else:
    print("It's not a palindrome")