class Sender:
    flag = False

    @classmethod
    def report(cls):
        if not cls.flag:
            print("yessss")
            cls.flag = True
            return
        else:
            print("noup")


class Asker:
    @staticmethod
    def askall(lst):
        for i in lst:
            i.report()


lst = [Sender(), Sender(), Sender()]
ask = Asker()
# print(Asker.askall(lst))
Asker.askall(lst)