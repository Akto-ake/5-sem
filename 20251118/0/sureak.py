# Сериализация

s = {1, 2, 3, 4, 5}
import pickle
print(pickle.dumps(s))
t = pickle.dumps(s)
del s
new_s = pickle.loads(t)
print(new_s)

# B) сериализация экземпляра класса
# {i} класс с сериализацией

# реализуйте класс SerCls с полями lst (список), dct (словарь), num (число), st (строка)
# cоздайте экземпляр ser этого класса с непустым наполнением всех полей
# сериализуйте ser в строку, удалите ser
# десериализуйте строку в новый экземпляр ser1 класса SerCls
# выведите все поля объекта ser1
# * повторите действия, но теперь удалите ещё и класс. А потом пересоздайте его. А потом задайте новый с теми же полями. 
# А потом задайте пустой, но с тем же именем

class SerCls:
    def __init__(self, lst, d, n, str):
        self.lst = lst
        self.dct = d
        self.num = n
        self.st = str

    def __str__(self):
        return f'list: {self.lst}, dict: {self.dct}, num: {self.num}, st: {self.st}'

ser = SerCls([1, 2, 3], {'a': '0', 'b' : 9}, 666, 'heellp')
ser_n = pickle.dumps(ser)
del ser
ser1 = pickle.loads(ser_n)
print(ser1)

del SerCls
# ser2 = pickle.loads(ser_n)
class SerCls:
    lst = 'Gi'
    dct = 1337
    num = ()
    st = 'QQ'

ser2 = pickle.loads(ser_n)
print(ser2.lst)