thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #kutangra pana cherry


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #exclude kiwi


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


thistuple = ("apple", "banana", "cherry")
print(thistuple)


a= ["apple", "banana", "cherry", "apple", "cherry"]
print(a.index('apple'))



b= ["apple", "banana", "cherry", "apple", "cherry"]
print(b[1:4:2])


c="hello"
print(c[-1: :-1])





hislist = ["apple", "banana", "cherry"]
thislist[0:3:2] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]



thistuple = ("apple", "banana", "cherry")
print(len(thistuple))




thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))



tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)



myset = {"apple", "banana", "cherry"}



thisset = {"apple", "banana", "cherry"}
print(thisset)



set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set1.update("set2")



a = {
  "make": "toyota",
  "color": "blue",
  "model": "auris"
}
print(a["make"])
print(a["color"])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the chang




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

