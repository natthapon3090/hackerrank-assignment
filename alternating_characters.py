def alternating_characters(s:str)->int:

    count=0

    for i in range(1,len(s)):

        if s[i]==s[i-1]:
            count+=1

    return count
