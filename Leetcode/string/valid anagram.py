s = input()

t = input()


def characterCounter(s):
    counter = {}
    for character in s: 
        if character not in counter:
            counter[character] = 0
        counter[character] += 1
    return counter

def valid_anagram(s,t):
    counter1 = characterCounter(s)
    counter2 = characterCounter(t)
    return counter1 == counter2


print(valid_anagram(s,t))