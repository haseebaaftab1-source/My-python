list1 = [9,8,7,6,5,4]
print(list1)

list1.append(2)
print(list1)

list1.pop(4)
print(list1)

tuple1 = ("haseeba","nimra","amna","muzna")
print(tuple1)

print(type(tuple1))
for x in tuple1:
  print(x)

set1 = {7,8,9,3,4,5}
print(set1)
set2={2,3,4,5,6,}

#union

set3 = set1.union(set2)
print(set3)

#intersection

set3 = set1.intersection(set2)
print(set3)

#insubset
set3 = set1.issubset(set2)
print(set3)

#isdisjoint

set3 = set1.isdisjoint(set2)
print(set3)

#dictionary

dict1  = {"name":"haseeba aftab",
          "age":21,
          "degree":"BSIT",
          "roll no":675}
print(dict1)
print(type(dict1))

#updation

dict1["degree"] = "bs semester 5th"
print(dict1)

print(len(dict1))

dict2 = dict1.copy()
print(dict2)

del dict1["age"]
print(dict1)

#palindrome
list9 = [1,2,1]
if list9 == list9[::-1]:
  print("list is palindrome")
else:
  print("list is not palindrome")

