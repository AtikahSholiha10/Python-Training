file = open("processing.txt","r") 
print(file.read())

file = open("processing.txt","w") 
file.write("Ini adalah text yang baru")
file.close()

file = open("processing.txt","a") 
file.write("\nIni adalah teks yang ditambahkan")
file.close()