# Mantap

#FUNGSI F11, FUNGSI MELIHAT KRITIK SARAN

def lihat_laporan():
    print("Kritik dan saran:")
    arrayy = (pilihan("kritiksaran.csv")[1:]) #Array yang menampung data kritik saran tanpa baris pertama

    #Mengukur jumlah kolom
    length=0
    for row in arrayy:
        length+=1

    # Menampung ID wahana ke dalam array
    array = [0 for i in range(length)]
    i=0
    for row in (arrayy):
        array[i] = row[2]
        i+=1

    mini = 0 #Menyatakan nilai i terkecil
    #Fungsi Sort Kode
    for x in range(length):
        min = "[[[[[["
        for i in range(length):
            if array[i] <= min:
                min = array[i]
                mini = i

        #Output sesuai dengan urutan yang sudah di sort
        print((arrayy[mini])[2] + " | " + (arrayy[mini])[1] + " | " + (arrayy[mini])[0] + " | " + (arrayy[mini])[3])
        #Set nilai yang sudah di sortir menjadi nilai yang pasti lebih besar terbesar agar bisa dibandingkan
        array[mini] = "[[[[[["
        min = "[[[[[["
    return
