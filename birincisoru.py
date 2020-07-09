tarih = input ("Tarih giriniz örn(04-05-2020)")
aylar = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
ay = (tarih.split("-"))
i= 1
if(int(ay[0])>31 or int(ay[1])>12): #Gün 31'den bütük, ay 12'den büyük girilemez
    print ("Hatalı giriş")
else:
    while i<=12:
        if(i>=10):
            if(ay[1] == str(i)):
                print (ay[0]+" "+aylar[i-1]+" "+ay[2])
        else:
             if(ay[1] == "0"+str(i)):
                print (ay[0]+" "+aylar[i-1]+" "+ay[2])
        i=i+1
input() #Program exe olarak çalıştırılırsa çalışmasının devam etmesi için yazdım
