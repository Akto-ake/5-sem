import struct

a = [123, 45, b'hello']

# b = struct.pack('ih5s', *a) #int, short, 5s - 5byte

with open('file4', 'bw+') as f:
    b = struct.pack('ih5s', *a)  # 11 byte
    b = struct.pack('h5si', 45, b'hello', 123) #12 byte, т.к. есть выравнивание
    print(b)
    f.write(b)

# прочитать тройки float, bytes[3], int из файла,
# записать их в файл с сетевым порядком байтов
import random

with open('random_file5', 'wb+') as f:
        seq = [(random.random(), bytes(random.sample(range(5),3)),
                random.randrange(10000)) for i in range(10)]
        print(seq)
        for i in range(10):
            d = struct.pack('f3si', *seq[i])
            print(d, end = '\n')
            f.write(d)