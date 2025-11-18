import sys 

# Командная строка и sys.argv

# {i} Вывести все параметры командной 
# строки в отсортированном виде

# print(*sorted(sys.argv))

# ---------------------------

# with open('o', 'w+') as file:
#     print("hello world!\n Im student\npupupu\n111\n2222\n", file = file)

with open('o', 'rb') as file: #считаем в бинарном виде
    print(file.readlines())

# допишем в тот же файл в конец значения

with open(sys.argv[1], 'r+') as file:
    print(*sorted(file.readline()), file=file)

# with open('file1', 'br') as file:
#     file.seek(0, 10) #прыгаем первое - на сколько, второе - откуда
#     for i in range(40):
#         file.read(1)
