# Multiple Inheritance
# DIamond Problem-- Same fun name, which one it will call
# Method Resolution Order- MRO which ever is the first one will be called first

class Father:
    def father_money(self):
        return 5

    def home(self):
        return "This is from the father"


class Mother:
    def mother_money(self):
        return 2

    def home(self):
        return "This is from the mother"


class Son(Mother, Father):  # Son will have home of Mother because first Mother is written first
    pass


class Son2(Father, Mother):  # Son will have home of Mother because first Father is written first
    pass


s = Son()
s2 = Son2()
print(s.father_money())
print(s.mother_money())
print(s.home())
print(s2.home())
