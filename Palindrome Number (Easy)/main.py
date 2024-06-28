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


# def isPalindrome2(x):
#     is_palindrome = False

#     if x<0:
#         return is_palindrome
    
#     if len(str(x))%2==0:
#         y = int(len(str(x))/2)
#         print(str(x)[y::][::-1], str(x)[:y:])
#         if str(x)[y::][::-1] == str(x)[:y:]:
#             is_palindrome = True
#     elif len(str(x))%2!=0:
#         y = math.ceil(len(str(x))/2)

#         if str(x)[y::][::] == str(x)[y::]:
#             is_palindrome = True

#     return is_palindrome

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
        


print(isPalindrome2(121))