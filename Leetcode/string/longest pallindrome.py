
s = "bananas"

def character_counter(s):
    counter = {}
    for i in range(0,len(s)):
        counter[s[i]] = 1 + counter.get(s[i],0)
    return counter 

def longest_pallindrome(s):
    counter = character_counter(s)
    if(len(counter) == 1):
        first = list(counter.values())
        return first[0]
    answer = 0;
    usedSingle = False
    for (value,index) in counter.items():
        if(index % 2 == 0 or index > 2):
            answer += int((index/2))*2
        if(index % 2 != 0) and not usedSingle:
            answer+=1
            usedSingle = True
    return int(answer)

print(longest_pallindrome(s))