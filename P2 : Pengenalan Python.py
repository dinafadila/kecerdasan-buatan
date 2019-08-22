# nomor 1
'''
def jumlah(a,b):
	return a+b
 print (jumlah(5,1))
'''

# nomor 2
'''
def jumlah1(a,b):
	return a+b
def jumlah2(a,b):
	print(a+b)

a = jumlah1(2,3)	#print a ada hasilnya
print(a)
b = jumlah2(2,3)	#print b none karna nilai jumlah2 gak ada return 
print(b)
'''

#nomor 3
'''
def biodata(nama, prodi, status='Mahasiswa S1'):
	print("Nama	: %s"%nama.capitalize()) 
	print("Prodi	: %s"%prodi.capitalize())
	print("Status	: %s"%status.capitalize())
	
biodata('dina', 'ilmu komputer')				#kalo ga di set statusnya ikutin default
biodata('dina', 'ilmu komputer', 'alumni')
'''

#cara print
'''
a=5
b=3
print("a :",a)
print("b : %d"% b)
print("b : {}".format(b))
print("ab : %d %f"%(a,b))
'''


#nomor 4
'''
def function(a,b,c):
	return a,b,c

print(function(1,2,3))			#kalo depannya samadengan, seterusnya sama dengan
print(function(a=1,b=2,c=3))	#kalo depannya gak sama dengan, belakangnya bisa sama dengan atau tidak sama dengan
print(function(1,b=2,c=3))
'''

#nomor 5
'''
def nilai(nama,prodi, *skor):
	print("Nama	: %s"%nama.capitalize())
	print("Prodi	: %s" %prodi.capitalize())
	print("Skor	:",skor)
	for i in range(len(skor)):
		print("Skor ke-{} = {}".format(i,skor[i]))
		
nilai("budi","ilmu komputer", 90,80,70,50,"selesai")
'''

#nomor 6
'''
keywords = {
	"a" : 1,
	"b" : 2,
	"c" : 3
}

print(list(keywords.keys())) #buat ambil variable
print(list(keywords.values())) #buat ambil nilainya
'''

#nomor 7 kepemilikan variable
'''
x = 50
def fungsi(i):
	x = i**2	#varible lokal
	print ("x di variable lokal :",x)

fungsi(5)
print("x di varible global :", x)	# kalo udah keluar dari fungsi dia bakal ngikutin variable global
'''

#nomor 8 manggil fungsi pake fungsi lain
def kuadrat(x):
	print("masuk ke fungsi kuadrat")
	return x**2
def apply(i,j):
	print("masuk ke fungsi apply")
	return i(j) #return kuadrat(2)
	
print(apply(kuadrat,2))


	





