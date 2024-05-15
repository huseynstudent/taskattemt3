tekler=0
cutler=0
for i in range(10):
      eded=int(input("ededi daxil edin"))
      if eded%2==0:
            cutler+=10
      elif (eded-1)%2==0:
            tekler+=10
print("cütlərin faizi:",cutler,"%")
print("təklərin faizi:",tekler,"%")
"""tapsiriq7"""
num=int(input("ədədi daxil edin "))
reversed=0
number=num
while num>0:
      step=num%10
      num//=10
      reversed=reversed*10+step
if number==reversed:
      print("bu eded polidromdur")
else:
      print("bu eded polidrom deyil")
"""tapsiriq8 i yaza bilmedim,zehmet olmasa dersde deyersiz"""

# num1=int(input("ededi daxil edin: "))
# num2=int(input("ededi daxil edin: "))
# reversed=0
# for n in range(num2):
#       step=num1%100
#       num1//=100
#       reversed=reversed*10+step
# print(reversed)

"""tapsiriq9"""   
bolunen=0
for eded in range(1,100):
      for num in range(1,eded):
            if eded%num==0:
                  bolunen+=1
      if bolunen==1:
            print(eded)
            bolunen=0
      else:
            bolunen=0
"""tapsiriq10"""
il = int(input("ili daxil edin"))
ay = int(input("ayı daxil edin"))
if ay==1:
      ay1=0
elif ay==2:
      ay1=31
elif ay==3:
      ay1=59
elif ay==4:
      ay1=90
elif ay==5:
      ay1=120
elif ay==6:
      ay1=151
elif ay==7:
      ay1=181
elif ay==8:
      ay1=212
elif ay==9:
      ay1=243
elif ay==10:
      ay1=273
elif ay==11:
      ay1=304
elif ay==12:
      ay1=334
gun = int(input("günü daxil edin"))
fevral_29=il//4
cem=(il*365+ay1+gun+fevral_29-2)
hefte=cem%7
if hefte==0:
      hefte=7
print(hefte,"-ci gundur")