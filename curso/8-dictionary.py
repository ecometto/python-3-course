data = {"name":"Edgardo", "age":44}
capitals={"Argentina":"BsAs", "Colombia":"Bologtá", "Chile":"santiago"}

print(data)
print(capitals)

print(data["name"])
print(capitals["Chile"])

data["nationality"] = "Argentina"
print(data)

del capitals["Chile"]
print(capitals)

print(capitals.get("Argentina", "The country was not found"))

keys = data.keys()
print(type(keys))

for each in keys:
    print(f"The key is {each}")

values = data.values()
print(values)