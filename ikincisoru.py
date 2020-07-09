sayi = input("Sayı Giriniz = ")
i = 0
y = 1
toplam = 0
faktoriyel=1
if int(sayi)>=16 or int(sayi)<0:
    print("Hatalı Değer Girdiniz")
elif(int(sayi)<9):
   while y<=int(sayi)*3:
       faktoriyel*=y
       y+=1
   print("3*"+str(sayi)+"! = "+str(faktoriyel))
else:
    while i<=int(sayi)*2:
        toplam+=i
        i+=2
    print ("Toplam = "+str(toplam))
input() #Program exe olarak çalıştırılırsa çalışmasının devam etmesi için yazdım
