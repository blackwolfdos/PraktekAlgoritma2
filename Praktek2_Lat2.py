import math

Lintang1 = math.radians(float(input("Lintang Kota 1: ")))
Bujur1 = math.radians(float(input("Bujur Kota 1: ")))
Lintang2 = math.radians(float(input("Lintang Kota 2: ")))
Bujur2 = math.radians(float(input("Bujur Kota 2: ")))

R = 6371
Lat = Lintang2 - Lintang1
Long = Bujur2 - Bujur1

a = math.sin(Lat/2)**2 + math.cos(Lintang1) * math.cos(Lintang2) * math.sin(Long/2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
d =  R * c

print("Jarak antara dua titik tersebut adalah ", d, "kilometer")
