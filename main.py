mylist = [12,5,12,666,15,23,10,10,11,5]
mylist1 = (12,5,12,666,15,23,10,10,11,5)
mylist2 = [5,6,4,7,8]

mylist.insert(3,55)
mylist.remove(666)
mylist.append(88)
mylist.extend(mylist2)
mylist.pop(6)
mylist.extend(mylist1)


result = 0

print("this is list ",mylist)
for x in mylist:
    result += x


mylist1[1] == 15
print("this is tuple ",mylist1)
for y in mylist:
    print("this is tuple ",y)

listset = {1,2,3,4,5,1,2,6,7,4}
print(listset)
thisset = {"apple", "banana", "cherry", "apple"}
thisset.add("orange")
thisset.remove("cherry")
print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


thisdic = {
    "car": "Mustang",
    "model": 1988,
    "speed": 250,
    "year" : 2005,
    "year": 2006,
    "year":2008

}

print(thisdic)
print(thisdic["car"])
print(thisdic["speed"])

print(len(thisdic))


a = [10,13,12,20,5]
b = [12,10,11,25,5]

a.extend(b)

print(a)

index = 0
total = 0
while index < len(a):
    total = total + a[index]
    index += 1

print(total)