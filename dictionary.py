dict = {
    "name": "John",
    "name1": "John",
    "name2": "John",
}

print(dict["name"])

#del 
del dict["name1"]

#get, returns none instead of throwing error 
dict.get('name1') 

#movie schedules

# schedules = {
#     'movie1': 'Intersteller',
#     'movie2': 'Intersteller2',
#     'movie3': 'Intersteller3',
# }
# user_input = input('what movie you want to watch ?')

# watch = schedules.get(user_input)
# if(watch):
#     print(watch)
# else:
#     print('This movie is not playing')


contacts = {
    'number':4,
    'students':[
        {'name':'imran', 'age':'12'},
        {'name':'imran2', 'age':'13'},
        {'name':'imran3', 'age':'14'},
    ]
}

nums = [1,2,3,4,2,3,4]
counter = {number: nums.count(number) for number in nums}
print(counter)
#
for contact in contacts['students']:
    print(contact['name'])

for key,value in contacts.items():
    print(key,value)

# get the first value from the dictionaryu 

first = list(counter.values())[0]

# sort a dictionary based on their value 

counter = {1:3,2:2,3:1}
counter = sorted(counter.items(),key=lambda item:item[1])
counter = {'A':1,'B':2}
del counter['A']
print(counter)
