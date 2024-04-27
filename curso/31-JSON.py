import json

# #tomando un formato STR (JSON) para convertirlo a DICT
# jsonStr = '{"name":"Edgardo", "age":33, "country":"Argentina"}'
# print(type(jsonStr))
# print(jsonStr)

# DictFromStr = json.loads(jsonStr)
# print(type(DictFromStr))
# print(DictFromStr)
# print(DictFromStr['name'],DictFromStr["age"], DictFromStr['country'], )

# #tomando un formato DICT para convertirlo a STR (JSON)
# myDict = {
#     "name":"Edgard",
#     "age":"32",
#     "country":"Arg",
#     "hobbies": ["play", "run", "fly"]
# }
# print(type(myDict))
# print(myDict['name'], myDict['age'], myDict['country'])

# myJson = json.dumps(myDict)
# print(type(myJson))
# print(myJson)

# #codificando y decodificando directamente
# # #pasando de formato DICT a JSON
# jsonJson = json.JSONEncoder().encode(
#     {
#         "cursos":["a ver que sale", "otro"],
#         "year":2024
#         }
#     )
# print(type(jsonJson))

# #pasando de formato JSON a DICT
# jsonDictionary = json.JSONDecoder().decode('{"cursos":["JS","HMTL","CSS"]}')
# print(type(jsonDictionary))

jsonFile = open("curso/31-json.json", "r")
jsonText = jsonFile.read()
jsonFile.close()

#print(jsonText)
DictObj = json.JSONDecoder().decode(jsonText)
#I'll modify dict object and then i'll replace the data in original json file
for each in DictObj:
    if each['country'] == "Argentina":
        each['country'] = "Argentina Latina"

newTextForFile = json.JSONEncoder().encode(DictObj)
jsonFile = open("curso/31-json.json", "w")
jsonFile.write(newTextForFile)
jsonFile.close()
