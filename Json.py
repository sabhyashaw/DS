import json

# 1
json_str = '{"name": "Sabhya", "age": 22}'
py_dict = json.loads(json_str)
print(py_dict)

# 2
py_dict = {"name": "Sabhya", "age": 22}
json_str = json.dumps(py_dict)
print(json_str)

# 3
with open("data.json", "r") as f:
    data = json.load(f)
print(data)

# 4
data = {"name": "Sabhya", "age": 22}
with open("output.json", "w") as f:
    json.dump(data, f)

# 5
data = {"b": 2, "a": 1, "c": 3}
sorted_data = dict(sorted(data.items()))
print(sorted_data)
