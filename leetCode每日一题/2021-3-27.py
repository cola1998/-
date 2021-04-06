def lengthOfLongestSubstring(s):
    if len(s) == 0 or len(s) == 1:
        return len(s)
    temp = ""
    max_length = 0
    for i in range(len(s)):
        if s[i] not in temp:
            temp += s[i]
            max_length += 1
        else:
            max_length = max(max_length, len(temp))
            index = temp.index(s[i])
            temp = temp[index + 1:]
            temp += s[i]
    return max_length
lengthOfLongestSubstring("au")