NIM = "1800018096"
NAMA = 'Atikah Zakiyyah Sholiha'

print(NAMA +" memiliki NIM "+ NIM)
print("Selamat datang di \"Coding!\"")

#string methods (sudah tersedia)

text = "Atikah Sholiha"
print(text.upper())
print(text.lower())
print(len(text))
print(text.split(' '))
print(text.index('S'))

#slicing index

print(text[0])
print(text[2:])
print(text[:5])
print(text[3:7])
print(text[-3])
print(text[-2:-8])

#string concatenation
x = "atikah"
y = "sholiha"

print(x+y)
print(x + " " + y)
print(x + " " + y + " " + str(1800018096))

#string format
text = "{} memiliki nim {} sudah lulus"

print(text.format(NAMA,NIM))

apel = 1
mangga = 3
pisang = 5
text = "Saya membeli {} apel, {} mangga, dan {} pisang"

print(text.format(apel, mangga, pisang))

#in
text = "Atikah Sholiha"
print("Sholiha" in text)
print("Tikah" in text)

