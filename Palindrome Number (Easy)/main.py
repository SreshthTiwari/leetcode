# convert to srting, O(n)

def isPalindrome(x):
    is_palindrome = False

    if x<0:
        return is_palindrome
    
    if str(x) == str(x)[::-1]:
        is_palindrome = True

    return is_palindrome

# reverse only half of number

import math

def isPalindrome2(x):
    is_palindrome = False

    if x<0:
        return is_palindrome
    
    if len(str(x))%2==0:
        y = int(len(str(x))/2)
        print(str(x)[y::][::-1], str(x)[:y:])
        if str(x)[y::][::-1] == str(x)[:y:]:
            is_palindrome = True
    elif len(str(x))%2!=0:
        y = int(math.ceil(len(str(x))/2))
        print(str(x)[y::][::-1], str(x)[:y-1:])
        if str(x)[y::][::-1] == str(x)[:y-1:]:
            is_palindrome = True

    return is_palindrome
        
# no converting to string, using integer

def isPalindrome3(x):
    if x<0 or (x%10==0 and x>0):
        return False
    reverse_number = 0
    while x>reverse_number:
        reverse_number = reverse_number*10 + x%10
        x//=10
    print(reverse_number, x)

    return True if (reverse_number == x or x == reverse_number//10) else False

print(isPalindrome3(12121))