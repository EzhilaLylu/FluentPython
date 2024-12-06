from datetime import datetime

# python has builtin function iter(). when we pass it a collection, we get an iterator object
# iter() called automatically when we access collection with for statement
# iterable vs iterator - input to iter() is iterable while output is iterator

numbers = [1, 2, 3, 4, 5, 6]

iterator_obj = iter(numbers)

next(iterator_obj) # get the next item in the iterator

# when the sequence completes StopIteration Error will get raised

# to avoid StopIteration and give in default value
for d in range(10):
    print(next(iterator_obj, "End reached"))

# Generator functions are coroutine. Regular function can have multiple exit points via return statements and has only one entry point. A coroutine is like a function, except it has several entry points. Yield statement creates exit point and re-entry points'/]'
# Generator functions Pros
# Generator functions are shortcut for creating iterators

def get_lylu_occurence(): #notice there is no return statement
    with open('text_doc.txt') as file_handle:
        for line in file_handle:
            if 'lylu' in line.lower():
                yield line


for data in get_lylu_occurence():
    print(data)


## composable interface

def read_file(path):
    with open(path) as file:
        for line in file:
            yield line


def house_records(lines):
    record = {}
    for line in lines:
        if line.strip() == '':
            yield record
            record = {}
            continue
        key, value = line.split(': ', 1)
        record[key] = value
    yield record

lines = read_file('address_data.txt')

# single line for loops
for house in house_records(lines): print(house['address'])


# syntactic advancement
"""
for house in house_records(lines):
        yield house

can be replaced with 

yield from house_records(lines)
"""
# yield from statement is used specifically in generator functions, when they yield values directly from another generator object


'''
Infusing your Python code with generators has a profound effect. All the code you write becomes more memory-efficient, more responsive, and more robust. Your programs are automatically able to gracefully handle larger input sizes than you anticipated
'''