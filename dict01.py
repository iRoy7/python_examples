dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingradient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin":  "필리핀"
}

print("name: ", dictionary["name"])
print("type: ", dictionary["type"])
print("ingradient: ", dictionary["ingradient"])
print("origin: ", dictionary["origin"])
print()

dictionary["name"] = "8D 건조 망고"
print("name: ", dictionary["name"])

dictionary["price"] = 5000

print("After add new element: ", dictionary)

key = input("> 접근하고자 하는 키: ")

if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

#get
value = dictionary.get("name");
print("value: ", value)
value = dictionary.get("존재하지 않는 키")
print("value: ", value)


# none
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")


for key in dictionary:
    print(key, ":", dictionary[key])


#items
example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}

print("# items() function of dictionanry")
print("items(): ", example_dictionary.items())
print()

print("# combination of items() and iterate statement")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))

    