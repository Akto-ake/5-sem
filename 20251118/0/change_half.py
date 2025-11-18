# поменять местами половины бинарного файла

with open("file1", "rb") as file:
    data = file.read()
with open("file1_change", "wb") as file:
    file.write(data[len(data) // 2 + 1:])
    file.write(data[:len(data) // 2 + 1])

#красивее:
with open("file1", "rb") as file:
    data = file.read()
    with open("file1_change2.0", "wb") as foo:
        print(data)
        foo.write(data[len(data) // 2:] + data[:len(data) // 2])
