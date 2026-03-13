import time
from datetime import datetime
import datetime as dt


import random
mass = [random.randint(5,30) for _ in range(10)]
print('mass',mass)

meeting_time1 = dt.datetime.now()

mass0 = map(lambda x: x * 2, mass)
mass0 = list(mass0)
print(mass0)

end_time1 = dt.datetime.now()
print(end_time1 - meeting_time1)

meeting_time2 = dt.datetime.now()

mass0 = [i**2 for i in mass]
print(mass0)

end_time2 = dt.datetime.now()
print(end_time2 - meeting_time2)




print('30 str')

mass = [
  (1,3,5),
  (12,8,10),
  (3,9,6)
]

for _ in mass:
  for index, i in enumerate(_):
    print(index,i)

print('42str')

i = 0

while True:
  try:
    for index,_ in enumerate(mass[i]):
      print('M',index,_)
    i+=1
  except:
    break

print()

import pdb
def f(x):
    print(1 / x)
#pdb.run("f(2)")


print(bytes(5))
print(len(bytes(5)))

print()
grocery_list = [5, 6, 7]

print(bytes(grocery_list))
print(len(bytes(grocery_list)))


fact = compile('print("Codecademy Docs is a great learning tool!")', 'test', 'eval')

eval(fact)


print()

import json

def process_config(config_data):

  config = {
    "max_connections": "50 * 2",
    "timeout_seconds": "30 + 15",
    "cache_size": "1024 * 1024",
    "debug_mode": "True"
  }

  processed_config = {}

  safe_globals = {"__builtins__": {}}
  safe_locals = {"True": True, "False": False}

  for key, value in config.items():
    try:
      processed_config[key] = eval(value, safe_globals, safe_locals)
      print(f"{key}: {value} -> {processed_config[key]}")
    except:
      processed_config[key] = value
      print(f"{key}: {value} (kept as string)")

  return processed_config

result = process_config({})

print()

hashable_tuple = (1, 2, 3, "hello")
hashable_string = "Python"
hashable_number = 103.0
hashable_number2 = 103.12

print(f"Tuple hash: {hash(hashable_tuple)}")
print(f"String hash: {hash(hashable_string)}")
print(f"Number hash: {hash(hashable_number)}")
print(f"Number hash: {hash(hashable_number2)}")


mutable_list = [1, 2, 3]
mutable_dict = {"key": "value"}

try:
  print(f"List hash: {hash(mutable_list)}")
except TypeError as e:
  print(f"Error hashing list: {e}")

try:
  print(f"Dict hash: {hash(mutable_dict)}")
except TypeError as e:
  print(f"Error hashing dictionary: {e}")

print()

arr = [1, 100, -200, 5834]

arr0 = []
for n in arr:
    print(hex(n))
    arr0.append(int(hex(n),16))

print(arr0)

print()


color = 'green'
favColor = 'green'
print(id(color)==id(favColor))

print()

data = [1, 2, 3]

p = [tuple,set,list]
for _ in p:
    if isinstance(data, _):
        print(f"List or tuple {_}")
    else:
        pass

