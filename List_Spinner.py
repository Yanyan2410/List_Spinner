List_awal = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

def counterClockwise(angka):
    if angka == "1":
        hasil = ""
        for i in range(3,0,-1):
            if i == 3:
                for j in range (1,10):
                    if j%3 == 0:
                        hasil += f"{j} "
            else:
                for j in range(1,10):
                    if j%3 == i:
                        hasil += f"{j} "
            hasil += "\n"
    elif angka == "2":
        hasil = ""
        for i in range (1,10):
            if i%3 == 0:
                hasil += f"{i}\n"
            else:
                hasil += f"{i} "
    else:
        hasil = "Pilihan tidak ada dalam opsi"
    return hasil

opsi = input("Masukkan pilihan (1/2): ")
print (counterClockwise(opsi))