matris={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
A = [[1,2,-1],  
       [2,5,2],  
       [-1,-2,2]]  
X = [[5,19,18], 
      [1,5,18],  
      [11,21,19]]  
sonuc = [[0,0,0],  
               [0,0,0],  
              [0,0,0]]  
for y in range(len(A)):  
   for  b in range(len(X[0])):  
       for s in range(len(X)):  
           sonuc[y][b] += A[y][s] * X[s][b]
print("--------X Matrisi = esraerkus--------")
print("--------Şifreleme Sonucu--------")
for i in sonuc:
   print(i)
input() #Program exe olarak çalıştırılırsa çalışmasının devam etmesi için yazdım
