class person:
    nama = "Atikah"
    usia = 22

orang = person()
print(orang.nama)
print(orang.usia)

class manusia:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def greet(self):
        print("Halo, "+self.name+"!")

p1 = manusia("Atikah",22,85)
p2 = manusia("Burhan",20,80)
print(p1.name)
print(p1.__dict__)
p1.greet()

class animal:
    def __init__(self, nama, kaki):#parent class
        self.nama = nama
        self.kaki = kaki

    def greet(self):
        print("hello!")

class cat(animal):#child class
    def __init__(self, nama, kaki, color, weight):
        super().__init__(nama,kaki)
        self.color = color
        self.weight = weight

class dog(animal): #child class
    def __init__(self,nama, kaki, type):
        super().__init__(nama,kaki)
        self.type = type

h1 = cat("katty",4,"putih",8)
h2 = dog("doggy",4,"bulldog")
print(h1.nama)
print(h2.__dict__)
