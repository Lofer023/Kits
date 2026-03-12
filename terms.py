# string = ['rooter','film','program']
# assert 'film2' in string, 'Not in string'
# assert 'program' in string, 'Not in string'

from datetime import datetime
import asyncio

async def function():
    await asyncio.sleep(0)
    return 1

async def function2():
    await asyncio.sleep(0)
    return 2

async def make():

    current_datetime = datetime.now()
    print(current_datetime)
    batch = asyncio.gather(function(),function2())
    func_complete, func2_complete = await batch
    end_datetime = datetime.now()

    print(end_datetime-current_datetime)
    print(func_complete)
    print(func2_complete)

result = asyncio.run(make())
print(result)

print()

class Person:
  def __init__(self, name):
    self.name = name

  def sayHi(self):
    # Calls its method .getName()
    print(f"Hi! My name is {self.getName()}.")

  def getName(self):
    # Accesses the name variable
    return self.name

bob = Person("Bob")
bob.sayHi()


def odd_numbers():
  start = 3
  for n in range(start,10):
    if n % 2 == 1:
      continue
    print(n)

print('odd')
odd_numbers()


import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def func2():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

        await task1, task2

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")

asyncio.run(func2())

print()

import asyncio

async def bas1(arg):
    print(arg)
    return arg

async def bas1feed():
    task = asyncio.create_task(arg)
    await task

arg = 42
arg = bas1(arg)
asyncio.run(bas1feed())

print()

import asyncio
from asyncio import TaskGroup

class TerminateTaskGroup(Exception):
    """Exception raised to terminate a task group."""

async def force_terminate_task_group():
    """Used to force termination of a task group."""
    raise TerminateTaskGroup()

async def job(task_id, sleep_time):
    print(f'Task {task_id}: start')
    await asyncio.sleep(sleep_time)
    print(f'Task {task_id}: done')

async def func3():
    try:
        async with TaskGroup() as group:
            # spawn some tasks
            group.create_task(job(1, 0.5))
            group.create_task(job(2, 1.5))
            # sleep for 1 second
            await asyncio.sleep(1)
            # add an exception-raising task to force the group to terminate
            group.create_task(force_terminate_task_group())
    except* TerminateTaskGroup:
        pass

asyncio.run(func3())



nabor = [
    [1,2,3],
    [13,9,21]
]

del nabor[1][1]
del nabor[0][0]

print(nabor)


m = 1

def funcvalidate(m):
    m = 1/m

try:
    funcvalidate(m)
    print('No division error')
except ZeroDivisionError as e:
    print('error',e)
else:
    print('end')

import sys
print(sys.argv)
print(sys.executable)
print(sys.getrecursionlimit())
print(sys.hash_info.inf)
print(sys.int_info.bits_per_digit)
print(sys.orig_argv)


f = open('text.txt','w')
f.write('Lorem ipsum \n dolor sit amet')
f.close()

f = open('text.txt','r')
read_data = f.readline()
print(read_data)
f.close()




def print_biography(name, country, age, hobby):
  print("Hello! My name is " + name + " and I'm " + str(age) +
        " years old. I come from " + country +
         ", and in my free time I like to " + hobby + ".")

adam = {
  "name": "Adam",
  "country": "Germany",
  "age": 23,
  "hobby": "paint"
}

print_biography(**adam)


with open('terms.txt','w') as f:
    file.read()
