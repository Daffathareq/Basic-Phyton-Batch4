my_sets = {"apel", "manggis", "pisang"}
print(type(my_sets))

#menginisialisasi set kosong
a = set()
print (type(a))

for x in my_sets:
    print(x)

#cek apakah ada di dalam sets
print ("apel" in my_sets)   

#nambah data di sets
my_sets.add("melon")
print(my_sets)

#menghapus data di sets
my_sets.remove("manggis")
print(my_sets)

my_sets2 = {1,2,3,4,5,1,4}
print(my_sets2)