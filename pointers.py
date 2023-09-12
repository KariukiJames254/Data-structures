dict1 ={
    'value': 11
}
dict2 = dict1

print("before value is updated:")
print("dict1= ", dict1)
print("dict2= ", dict2)

print("\ndict1 ponts to:", id(dict1))
print("dict2 points to:", id(dict2))