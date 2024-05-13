s = input("What's your name? ")
print(s)
print(len(s))
print(s[0])

# reverse a string 

reverse_string = s[3:1:-1]
print(reverse_string)

# remove all space
space_removed = s.replace(" ", "")

print(space_removed)

# make lowercase 

s = s.lower()

# allow only alpha numeric values 
s = ''.join([char for char in s if char.isalnum() ]) 


# loop with index and character 

for index,character in enumerate(s):
        print(index,character)

print(s[0:4:1])
print(s[0:0:1])