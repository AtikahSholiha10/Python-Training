def greet():
    print("hello stranger!")
    print("Good Morning")

greet()

def greet2(name,age):
    print("Welcome, "+name)
    print("You are "+str(age)+" years old")

greet2("Atikah",22)
greet2(age=20, name="burhan")

def tambah(x):
    x += 5
    return x

print(tambah(3))

x = 3
jumlah = tambah(x)
print(jumlah)

tambah = lambda x: x+5
print(tambah(x))

