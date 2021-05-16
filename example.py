import json

with open("bus_fake_data.json") as f:
  data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)