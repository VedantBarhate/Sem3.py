import json

# with open("sample1.json", 'r') as file:
#     data = json.load(file)
#     print(data)


# x = '{"name":"sahil", "class":"sy", "cgpa":7.3}'
# y = json.loads(x)
# print(y)

# data = {"name":"vedant", "class":"sy", "cgpa":8.8}
# with open("output.json", 'w') as file:
#     json.dump(data, file)


data = {"name":"vedant", "class":"sy", "cgpa":8.8}
data_s = json.dumps(data)
print(data_s)
print(type(data_s))