# O(n) hashmap

def romanToInt(s):
    one_values = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }

    num = 0

    for i in range(len(s)):
        if i<len(s) -1  and one_values[s[i]]<one_values[s[i+1]]:
            num -= one_values[s[i]]
        else:
            num += one_values[s[i]]

    return num

print(romanToInt("MCMXCIV"))