#keterangan mengenai program
print("Program Sederhana Untuk Cek Apakah Sebuah Bilangan Ganjil/Genap")
print("---------------------------------------------------------------")
print("Program ini akan menentukan apakah bilangan yang anda masukkan merupakan bilangan ganjil atau bilangan genap")
#input bilangan
bil = int(input("Masukkan Bilangan Anda: "))

#cek apakah bil habis dibagi 2, jika iya berarti bilangan genap
if(bil % 2 == 0):
    print(bil, "adalah Bilangan Genap")

#jika tidak, pasti bilangan ganjil
else:
    print(bil, "adalah Bilangan Ganjil")