#given a string we have to identify if its a palindrome or not 
# s = input()
s = 'A man, a plan, a canal: Panama'
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    s = [char for char in s if char.isalnum()]
    firstPointer = 0
    lastPointer = len(s)-1
    while(firstPointer < lastPointer):
        if(s[firstPointer]!= s[lastPointer]):
            return False
        firstPointer +=1 
        lastPointer -=1
    return True
print(is_palindrome(s))