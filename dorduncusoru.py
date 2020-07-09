y= 1
toplam = 0
ogrno = "1804107026"
asalsayilar = []
soniki = ogrno[-2:]
for sayi in range(y,int(soniki) + 1):
   if sayi > 1:
       for i in range(2,sayi):
           if (sayi % i) == 0:
               break
       else:
           toplam=toplam+sayi
           asalsayilar.append(sayi)
print("Öğrenci Numarası = "+ogrno)
print("Asal Sayılar Listesi = "+str(asalsayilar))
print("Asal sayı toplamı = "+str(toplam))
input() #Program exe olarak çalıştırılırsa çalışmasının devam etmesi için yazdım
