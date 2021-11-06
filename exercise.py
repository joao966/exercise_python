# exercise 01
# objeto = {"nome": "João", "idade": "25", "pais": "Brasil"}

# for prop in objeto:
#     print(prop)

# exercise 02
# def sum(a, b):
#     return a + b


# print(sum(2, 2))


# exercise_03
# def return_bigger(a, b):
#     if a > b:
#         print("a maior que b")
#     else:
#         print("b maior que a")


# return_bigger(0, 1)


# exercise_04
# def medium(array):
#     sum = int(array[0]) + int(array[1]) + int(array[2])
#     result = sum / len(array)
#     print(result)


# medium([10, 8, 5])

# exercise_05
# registers = [
#     {"name": "João", "idade": 25},
#     {"name": "Regina", "idade": 55},
#     {"name": "Ignês", "idade": 80},
#     {"name": "Hércules", "idade": 5},
# ]

# for cur in registers:
#     print(cur)

# exercise_06
registers = [
    {"name": "João", "stacks": ["JavaScript", "Python"]},
    {"name": "Regina", "stacks": ["HTML", "CSS"]},
    {"name": "Ignês", "stacks": ["React", "Redux"]},
    {"name": "Hércules", "stacks": ["MongoDB", "MySQL"]},
]

for cur in registers:
    for sub_key in cur["stacks"]:
        print(sub_key)
