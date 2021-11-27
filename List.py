# Akses list
## Menampilkan elemen ke-3
EXO = ['Suho', 'Sehun', 'Chanyeol', 'DO', 'Baekhyun']
print()
print("EXO :", EXO)
print()
print('Elemen ke-3', EXO[2])
print()

## Ambil nilai elemen ke-2 sampai ke-4
print('Elemen ke-2 sampai ke-4', EXO[1:5])
print()

## Ambil elemen terakhir
print ('Elemen terakhir', EXO[-1])
print()


print("=============================================================================")

# Ubah elemen list
## Ubah elemen ke-4 dengan nilai lainnya
Hewan = ['Kuda', 'kelinci', 'kucing', 'beruang', 'panda']
print()
print("Hewan sebelum di ubah:", Hewan)
print()
Hewan[3] = 'pinguin'
print("Hewan sesudah di ubah:", Hewan)
print()

## Ubah elemen ke-4 sampai dengan elemen terakhir
Hewan[3:] = ["Srigala", "Ular"]
print("ubah elemen ke-4 hingga akhir :", Hewan)
print()

print("=============================================================================")

# Tambah elemen list
## Ambil 2 bagian dari list pertama (A) dan jadikan list kedua (B)
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]

b.append(a[0:2])
print(b)

## Tambah list B dengan nilai string
print()
b.append("19")
print(b)

## Tambah list B dengan 3 nilai
print()
print(b + [20, 21, 22])

## Gabungkan list B dengan list A
print()
print(a + b)

print("=============================================================================")