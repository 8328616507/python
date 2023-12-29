# sreedhar
# 29-12-2023

list = ()
print(list)
list1 = (1, 2,)
print(list1)
Alist = (1, 2, 3, 45, 567,)
print(Alist)
Alist = Alist.index(3)
print("value:", Alist)
Blist = []
print(Blist)
clist = [1, 2, 3, 4, 5, 6, 6, 7]
print(clist)
print("the value:", clist[2])
dlist = [1, 2, "sreedhar", [1, 3, "sreedhar"], 4, 5, 6, 7, 8,]
print(dlist)
print("the size of list:", len(dlist))
flist = [1, 2, "sreedhar", [1, 3, "sreedhar", "bool", True, 1.0,], 4, 5, 6, 7, 8,]
print(flist)
print("the value:", flist[2])
print("the value:", flist[2][2])
print("the value:", flist[3][5])
print("the size of list:", len(flist))

# replace
sreedhar = ["sreedhar", "deva", "arun","pavan"]
sreedhar[3] = "basha"
print("the updated item :", sreedhar)
# sreedhar[4] = "basha"
# print("the updated item :", sreedhar)

# append

sreedhar = ["sreedhar", "deva", "arun", "pavan"]
sreedhar.append("sreedhar")
print("the append value is:", sreedhar)
sreedhar.append(["sreedhar", "deva", "arun"])
print("the append value is:", sreedhar)

# insert

sreedhar = ["sreedhar", "deva", "arun", "pavan"]
sreedhar.insert(0, "sree")
print("the new value:",sreedhar)

# pop

sreedhar = ["sreedhar", "deva", "arun", "pavan"]
sreedhar.pop()
print("enter the value:", sreedhar)

# pop()

sreedhar = ["sreedhar", "deva", "arun", "pavan"]
sreedhar.pop(3)
print("enter the value:", sreedhar)

# del

sreedhar = ["sreedhar", "deva", "arun", "pavan"]
del sreedhar[0:4]
print("enter the value:", sreedhar)

# clear

sreedhar = ["sreedhar", "deva", "arun", "pavan"]
sreedhar.clear()
print(sreedhar)





