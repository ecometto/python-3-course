list=["hello", "world", 34,67, True]

print(list[1:3])
print(list[1:])

list.append("bye")
print(list)

list.insert(0, "new")
print(list)

list.extend(["new list", 100])
print(list)

print(list.index("world"))

list.pop(2)
print(list)

del list[0]
print(list)

print(list*2)

#print(dir(list))

if "hello" in list:
    print("'Hello' exist in the list")
else:
    print("'Hello doesn't exist in the list")
    
