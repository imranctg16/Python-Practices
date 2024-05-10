class Process:
    def __init__(self):
        pass
    @staticmethod
    def characterCounter(s):
        counter = {}
        for character in s: 
            if character not in counter:
                counter[character] = 0
            counter[character] += 1
        return counter


