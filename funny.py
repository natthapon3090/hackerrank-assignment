def funny_string(s: str) -> str:
    reversed_s = s[::-1]

    for i in range(1, len(s)):
        diff1 = abs(ord(s[i]) - ord(s[i-1]))
        diff2 = abs(ord(reversed_s[i]) - ord(reversed_s[i-1]))

        if diff1 != diff2:
            return "Not Funny"

    return "Funny"

