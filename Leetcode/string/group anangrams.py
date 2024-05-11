
strings = ["eat","tea","tan","ate","nat","bat"]
strings = ["",""]
strings = ["c","c"]
strings = ["","b",""]

def characterCount(str):
    counter = {}
    for char in str:
        counter[char] = counter.get(char,0) + 1
    return counter
def findMykey(myValue,dict):
    for key,value in dict.items():
        if(myValue == value):
            return key
    return myValue

def groupAnagrams(strs):
    counterList = {}
    for string in strs:
        if string:
            counterList[string] = characterCount(string)
        else:
            counterList[string] = ""
    print(characterCount)
    mapper = {}
    mapperList = []
    stringMapper = {}
    for key,value in counterList.items():
        sortedKey = ''.join(sorted(key))
        stringMapper[key] = sortedKey
        if value in mapperList:
            mapper[sortedKey].append(key)
        else:
            mapper[sortedKey] = []
            mapperList.append(value)
    answerList = []
    for key,value in mapper.items():
        tempList = []
        mappedKey = findMykey(key,stringMapper)
        if value:
            tempList.append(mappedKey)
            for value_item in value:
                temp = findMykey(value_item,stringMapper)
                tempList.append(temp) 
        else:
            tempList.append(mappedKey)
        answerList.append(tempList)
    return answerList


def groupAnagrams2(strs):
    counterList = {}
    # if all the strings are empty, then return the 
    emptyList = set()
    for string in strs:
        emptyList.add(string)
    if(len(emptyList) == 1):
        return [strs]
    for string in strs:
        counterList[string] = characterCount(string)
    listed = list(counterList.values())
    answerList = []
    for list_item in listed:
        temp_list = []
        for key,value in list(counterList.items()):
            if(value == list_item):
                temp_list.append(key)
                del counterList[key]
        if(temp_list):
            answerList.append(temp_list)
    return answerList

def groupAnangrams3(strs):
    #using sorting 
    anangram_list = {}
    for string in strs:
        sorted_string = ''.join(sorted(string))
        if(sorted_string in anangram_list):
            anangram_list[sorted_string].append(string)
        else:
            anangram_list[sorted_string] = [string]
    return list(anangram_list.values())

print(groupAnangrams3(strings))