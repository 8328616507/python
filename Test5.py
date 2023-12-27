# sreedhar
# 27-12-2023

string = "sreedharsrsdfhftktkloiptututrtyfgtjyugdh"
print(string.upper())
print(string.lower())
print(string.islower())
print(string.isupper())
print(string.capitalize())
print(string.count("k"))
print(string.find("u"))
print(string.rfind("d"))
print(string.index('y'))

string = "   ***sreedhardevaarunkjhhbjjvbuhuerhrehjkb@@@   "
print(string)
string = (string.strip(" "))
string = (string.rstrip("@"))


# find if numbers is odd or even

num = 53
if (num % 2) == 0:
    print("the number is even:", num)
else:
    print("the number is odd:", num)


# for loop

for number in range(1, 51, 2):
    print("this is odd number:", number)

for number in range(2, 52, 2):
    print("this is odd number:", number)

# find vowels in the given number
emName = input("enter the name:")
print("the data is stored in name:", emName)
count=1
for strItr in emName:
    print("the vowels character in", count, "iteration is:")
    if(strItr.upper()=="A" or strItr.upper()=="E" or  strItr.upper()=="I"or strItr.upper()=="O" or strItr.upper()=="U"):
       print("the vowels is found it is position:", count, "and the vowels is:", strItr)
    count += 1

emName = input("enter the name:")
print("the data is stored in name:", emName)
count = 1

for strItr in emName:
    print("the vowels character in", count, "iteration is:")
    if(strItr.upper()=="U" or strItr.upper()=="O" or  strItr.upper()=="I"or strItr.upper()=="E" or strItr.upper()=="A"):
       print("the vowels is found it is position:", count, "and the vowels is:", strItr)
    count -= 1

















