# eded=int(input("ededi daxil edin "))
# for num in range(1,eded):
#       if eded%num==0:
#             print(num)
"""tapsiriq3"""
bolunen=0
eded=int(input("ededi daxil edin "))
for num in range(1,eded):
      if eded%num==0:
            bolunen+=1
if bolunen==1:
      print("bu eded sadedir")
else:
      print("bu eded sade deyil")
"""tapsiriq4"""

"""tapsiriq5"""
musbetler=0
menfiler=0
sifirlar=0
for i in range(10):
      eded1=int(input("ededi daxil edin"))
      if eded1<0:
            menfiler+=10
      elif eded1>0:
            musbetler+=10
      elif eded1==0:
            sifirlar+=10
print("menfilərin faizi:",menfiler,"%")
print("mesbətlərin faizi:",musbetler,"%")
print("0-ların faizi:",sifirlar,"%")