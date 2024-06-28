#hashmap and stack
#INCOMPLETE
def isValid(s):
    mappings = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    stack = []

    for i in s:
        if i in mappings.values():
            stack.append(i)
        elif i in mappings.keys():
            if not stack or stack.pop()!=mappings[i]:
                return False
    return True


print(isValid("(){}[]"))