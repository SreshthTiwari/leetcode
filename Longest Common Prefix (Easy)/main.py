def longestCommonPrefix(strs):
    ans = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(len(first)):
        if first[i]!=last[i]:
            return ans
        ans+=first[i]
    return ans
print(longestCommonPrefix(["hello", "helworld", "help", "helw", "helwwwwwzz"]))