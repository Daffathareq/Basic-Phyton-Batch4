UjianTeori = float(input("Nilai Ujian Teori :"))
UjianPraktek = float(input("Nilai Ujian Praktek :"))

if UjianTeori >= 70 and UjianPraktek >= 70 :
    print("Selamat, Anda Lulus!")
elif UjianTeori >= 70 and UjianPraktek < 70 :
    print("Anda Harus mengulang ujian praktek")
elif UjianTeori < 70 and UjianPraktek >= 70 :
    print("Anda Harus mengulang ujian teori")
else :
    print ("Anda harus mengulang ujian teori dan praktek.")              