# sreedhar
# 22-12-2023
#Topic = Comparison operator

a = 10
b = 20
c = 20
result = a == b
print("result:", result)
result = c == b
print("result:", result)

result = c != b
print("result:", result)
result = a != b
print("result:", result)


result = c <= b
print("result:", result)
result = a <= b
print("result:", result)


result = c >= b
print("result:", result)
result = a >= b
print("result:", result)


result = a > c
print("result:", result)
result = a > b
print("result:", result)


result = c < b
print("result:", result)
result = b < a
print("result:", result)


# logic operator

a = 24
b = 34
c = 34
print(a>b and b>c)
print(b > a and c > a)
print(b>a and c>b)

a = 24
b = 34
c = 34
print(a > b or b > c)
print(b > a or c > b)
print(b > a or a > c)


x = 10
y = 20
print(not (x <= y))

x = 10
y = 20
print(not (x >= y))





# membership operator


string = "hello sreedhar"
print("the character o is in string:", 'o' in string)
string = "hello ,sreedhar"
print("the character o is in string:", 'm' in string)



string = "Hello Sreedhar"
print("the character o is in string:", 'o'not in string)
string = "Hello Sreedhar"
print("the character o is in string:", 'm' not in string)

# conditions statement
# if statement
print("Exam result")
marks = 35
if marks >= 35:
    print("you pass ")

print("Exam result")
marks = 20
if marks >= 35:
    print("you pass ")
else:
    print("fail")


print("Exam result")
marks = 45
if marks >= 35:
    print("you pass")
elif marks > 45:
    print("good")

print("Exam result")
marks = 40
if marks >= 35:
    print("pass")
elif marks < 45 and 50:
    print("good marks")
else:
    print("fail")

