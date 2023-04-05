print("Merhaba Etiya")
print("Hoş geldiniz")

#yorum satırı

#değişkenler start
# metinsel,numeril, obje => çift tırnak ilgili verinin metinsel değer olduğunu belirtir

#string
text = "Merhaba "

print(text)
print(text)
print(text)
text = "Selam"
print(text)
print(text)

studentCount = "45" #string
print(studentCount)
studentCount =45 #int => integer
print(studentCount + 5)

aweragePoint = 25.5 #double,flooat, decimal
print(aweragePoint + 5)

isVerified= True #bool, boolean => true or false
print(isVerified)

print(type(text))
print(type(studentCount))
print(type(aweragePoint))
print(type(isVerified))

#değişkenler end

#operatörler start
number= 10
#matematiksel operatörler 
print(10 + 10)
print(number + number)

print(number - 5)

print(number / 2)

print(number * 5)

#mod operatörü => %  sol taraftaki değerin sağ taraftaki değere bölümünden kalan sonuç
print(number % 3)

print(number + ((10 -number) * (5/10)))

#mantıksal operatörler mantıksal operatörlerin geriye dönüş tipi booleandır bu yüzden true yada false döner
print(number == 10 ) # == eşitlik kontrol eder
print(number != 10)  # != eşit değildir kontrol eder

print(number > 10) # > büyüklük kontrolü
print(number >= 10)# >= büyük eşittir kontrolü

print(number < 10) # < küçüklük kontrolü
print(number <= 10)# <= küçük eşittir kontrolü



#operatörler end