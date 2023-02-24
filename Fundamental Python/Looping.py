#for
for i in range(6) : #(start=0, stop=6, step=1)
    print("Looping!")

for i in range(5, 25, 3) :   #range(start, stop, step)
    print(i)

for i in range(10, 20, 2) :
    if i == 18:
        break #terminate angka

    print(i)

for i in range(10, 20, 1) :
    if i%2 == 0:
        continue #skip

    print(i)

#while
nilai = 100
while(nilai >=0):
    print("Uang Sekarang : "+ str(nilai))
    nilai -= 10

print("Uang sudah habis")