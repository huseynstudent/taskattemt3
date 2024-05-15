"""tapsiriq1"""
eded1 = int(input("ilk ədədi daxil edin "))
eded2 = int(input("ikinci ədədi daxil edin "))
eded3 = int(input("üçüncü ədədi daxil edin "))
op = str(input("toplama: + \t vurma: * \n"))
if op =="+":
      print(eded1+eded2+eded3)
elif op =="*":
      print(eded1*eded2*eded3)
else: 
      print("siz yanlış operator daxil etmisiz")
"""tapsiriq2"""
eded1 = int(input("ilk ədədi daxil edin "))
eded2 = int(input("ikinci ədədi daxil edin "))
eded3 = int(input("üçüncü ədədi daxil edin "))
op = str(input("b = ən böyüyü,k = ən kiçiyi , o = onların ədədi ortası \n\t"))
b = 0
k=0
o = eded1/3 + eded2/3 + eded3/3
if eded1 <= eded2 <= eded3:
      b = eded3
      k = eded1
elif eded1 <= eded3 <= eded2:
      b = eded2
      k = eded1
elif eded2 <= eded3 <= eded1:
      b = eded1
      k = eded2
elif eded2 <= eded1 <= eded3:
      b = eded3
      k = eded2
elif eded3 <= eded2 <= eded1:
      b = eded1
      k = eded3
elif eded3 <= eded1 <= eded2:
      b = eded2
      k = eded3
if op =="b":
      print(b)
elif op =="k":
      print(k)
elif op =="o":
      print(o)
else: 
       print("siz yanlış operator daxil etmisiz")
"""tapsiriq3"""
metr = float(input("uzunluğu metrlə daxil edin "))
uzunluq = str(input("hansına çevirmək istəyirsinizsə omu yazın:\nmil,düym,yard\t"))
if uzunluq =="mil":
      print(metr*0.000621371192)
elif uzunluq =="düym":
      print(metr*39.3700787)
elif uzunluq =="yard":
      print(metr*1.0936133)
else: 
       print("siz yanlış vahid daxil etmisiz")