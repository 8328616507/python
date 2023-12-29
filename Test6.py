# sreedhar
# 28-12-2023

s = input("enter the name:")
sree = "a", "e", "i", "o", "u","A", "E", "I", "O", "U",
print("the data is stored in name:", s)
count = 1
result = s[::-1]
for i in result:
    print("the vowels character in", count, "iteration is:")
    if i in sree:
        print("the vowels is found it is position:", count, "and the vowels is:", i)
    count += 1

a = 1
while a < 1001:
    print(a, "sreedhar is a good parson")
    if a == 10:
        print(a, "sreedhar is nice and  poor man")
        break
    a += 1

a = 0
while a < 10:
    a += 1
    if a == 3:
        print(a, "value is 3")
        continue
print(a, "sreedhar is good parson ")

# find repeated character in string using for loop
name = input("enter the name:")
repeated_chars = []
lenofstring = len(name)
print("length of string:", lenofstring)
count = 1
for strItr in name:
   if (name.count (strItr)>1 and strItr not in repeated_chars):
       print("the repeated is found it is position:", count, "and the repeated is:", strItr)
   count+=1











