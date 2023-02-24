x = 5
y = 10
z = 15

print(not(x>y))
print(y>z)
print(x<y)

if x != y : #true
    print("x tidak sama dengan Y")

if x > z : #false
    print("X lebih besar dari Z")

if z <=y : 
    print("Z lebih kecil atau sama dengan Y") #true
else :
    print("Z lebih besar dari Y") #false

if x > y and x > z :
    print("X angka terbesar")
elif x > y or x > z :
    print("X angka tengah")
else :  
    print("X angka terkecil")