# A list comprehension is a high-level, declarative way to create a list

a_l = [0, 1, 2, 3, 4, 5, 6, 7, 8]

filtered = [data for data in a_l if data%2 == 0]
print(filtered)

filtered = [data if data%2 == 0 else '$' for data in a_l ]
print(filtered)

ff = [range(5), range(20,30,2)]
grouped = [data for sub in ff for data in sub if data > 10]
print(grouped)

# Generator expression

NUM_SQUARES = 10*1000*1000
generated_squares = ( n*n for n in range(NUM_SQUARES) )
print(next(generated_squares))

#  When passing a generator expression as an argument to a function, we can ignore surronding parentheses

sorted((user.email for user in all_users if user.is_active))
sorted(user.email for user in all_users if user.is_active)

# Dictionary comprehension
dc = { student.name: student.gpa for student in students }

# set comprehension
sc = { student.major for student in students }

# tuple comprehension is not there