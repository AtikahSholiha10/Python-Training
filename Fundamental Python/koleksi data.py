#list
array = ['Atikah', 1800018096, 3.65, True, 'A']

print(array[0])
print(array[1:4])
print(array[-2])
print(array)

array.insert(2,'informatika')
array.append('LULUS')
print(array)

#remove, pop, del, clear(semua)
array.remove('A')
array.pop() #paling akhir
print(array)

del array[4] #indeks
print(array)

aray = [1,2,5,7,8,10,12]
for item in aray:
    if (item %2 == 0):
        print(item)

if 10 in aray:
    print("Ada angka 10")

#method: len, copy, concat (+ dan extend), index, sort, reverse
aray = [5, 10, 55, 40, 20, 75, 80]
aray2 = aray.copy()

panjang =len(aray)
print(panjang)

aray2[0]=100
print(aray)
print(aray2)

#concat
aray = [5,15,30,50]
aray2 = [25,75,100]
print(aray+aray2)

aray.extend(aray2)
print(aray)

print(aray.index(15))

aray.sort()
print(aray)

aray.reverse()
print(aray)



