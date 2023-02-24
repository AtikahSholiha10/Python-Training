#tuple

tapel = ('atikah', 3.65, 1800018096, 'Lulus', True)
print(tapel)
print(tapel[1:3])

customer = {
    "nim" : 1800018096,
    "nama" : "Atikah Sholiha",
    "usia" : 22
}

customer["usia"]=23
customer["pekerjaan"] = "analyst"

print(customer)
print(customer["nama"])

customer.pop("nim")
print(customer)

#set (gaabungan, irisan, diference)

number1 = {1,2,5,7,10}
number2 = {2,3,4,5,10,12}

uni = number1.union(number2)
dif1 = number1.difference(number2)
dif2 = number2.difference(number1)
intrs = number1.intersection(number2)

print(uni)
print(dif1)
print(dif2)
print(intrs)

sym_dif = number1.symmetric_difference(number2)
print(sym_dif)


