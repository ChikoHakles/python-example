#impor library "calendar" untuk mengambil data hari per bulan
import calendar

print("Masukkan Tahun dan Bulan untuk memunculkan kalender")

#masukkan tahun dan bulan dalam angka
tahun = int(input("Tahun: "))
bulan = int(input("Bulan: "))

#tampilkan kalender
print(calendar.month(tahun, bulan))