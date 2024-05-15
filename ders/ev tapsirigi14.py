
"""funksiyalar"""
"""task1"""
eded=int(input("ededi daxil edin: "))
def kub(eded):
    eded*=eded*eded
    return eded
print(kub(eded))
"""task2"""  
eded1=int(input("ilk ededi daxil edin: "))
eded2=int(input("ikinci ededi daxil edin: "))
def muqayise(eded1,eded2):
    if eded1>eded2:
        print(eded1," daha böyükdür")
    elif eded2>eded1:
        print(eded2," daha böyükdür")
muqayise(eded1,eded2)
"""task3"""
num=int(input("ededi daxil edin: "))
def mueyyenlesdir(num):
    if num<0:
        return "yanlış"
    elif num>0:
        return "doğru"
    else:
        return "eded 0-dır"
print(mueyyenlesdir(num))
"""task4"""
num1=int(input("ilk ededi daxil edin: "))
num2=int(input("ikinci ededi daxil edin: "))
op=str(input("emeliyyatı daxil edin:(+,-,*,/)"))
def emeliyyat(num1,num2,op):
  def operator(sum):
      if op=="+":
              return(num1+num2)
      elif op=="-":
          return(num1-num2)
      elif op=="*":
          return(num1*num2)
      elif op=="/":
          return(num1/num2)
  print(operator(sum))
emeliyyat(num1,num2,op)
"""task5"""
uzunluq=int(input("uzunluğu daxil edin: "))
def kvadrat(uzunluq):
    for i in range(uzunluq):
        for j in range(uzunluq):
            if i==0 or j==0 or j==uzunluq-1 or i==uzunluq-1:
                print(end="*")
            else:
                print(end=" ")
        print()
kvadrat(uzunluq)
"""task6"""
bolunen=0
num=int(input("ededi daxil edin"))
for i in range(num):
    if num%(i+1)==0:
        bolunen+=1
if bolunen<=2:
    print(num," sadedir")
else:
    print(num," sade deyil")
"""task7"""
number=int(input("ededi daxil edin: "))
def faktor(num):
    yenieded=1
    for i in range(number):
        yenieded*=i+1
    return yenieded
print(faktor(number))
"""task8"""
ust=int(input("ədədin üstünü daxil edin: "))
quvvet=int(input("ədədin qüvətini daxil edin: "))
def hesablama(ust,quvvet):
    netice=1
    for i in range(quvvet):
        netice*=ust
    return netice
print(hesablama(ust,quvvet))
"""task9"""
number1=int(input("böyük ededi daxil edin: "))
number2=int(input("kiçik ededi daxil edin: "))
def araliq(num1,num2):
    for i in range(number1-number2-1):
        print(number2+i+1)
araliq(number1,number2)


print("random")
import random
say=0
def bolunme(say):
      say=0
      eded=[]
      for i in range(10):
            x=random.randint(1,100)
            eded.append(x)
      print(eded)
      for i in eded:
            if i%3==0 and i%5!=0:
                  say+=1
      return say
print(bolunme(say))
"""task2"""
ilk_menfi_index=-1
def menfi():
      eded=[]
      for i in range(10):
            x=random.randint(-10,30)
            eded.append(x)
      print(eded)
      for i in range(len(eded)):
            if eded[i]<0:
                  ilk_menfi_index=i
                  break
      cem=0
      for num in eded[ilk_menfi_index+1:]:
            cem+=num
      return(cem)
print(menfi())
"""task3"""
ilk_musbet_index=-1
def musbet():
      eded=[]
      for i in range(4):
            a=random.randint(-10,30)
            eded.append(a)
      print(eded)
      for i in range(len(eded)):
            if eded[i]>0:
                  ilk_musbet_index=i
                  break
      cem=0
      for num in eded[ilk_musbet_index+1:]:
            cem+=num
      return(cem)
print(musbet())
"""task4"""
def min_max(min,max):
      num=[]
      for i in range(20):
            a=random.randint(-1000,1000)
            num.append(a)
      print(num)
      num.sort()
      return num[0],num[-1]
print(min_max(min,max))
"""task5"""
def faiz():
      num=[]
      tekreqemli_ededler=0
      ikireqemli_ededler=0
      ucreqemli_ededler=0
      for i in range(20):
            a=random.randint(1,200)
            num.append(a)
      print(num)
      for i in num:
            if 1<=i<=9:
                  tekreqemli_ededler+=1
            elif 10<=i<=99:
                  ikireqemli_ededler+=1
            elif 100<=i<=200:
                  ucreqemli_ededler+=1
      print("tek reqemli ededler umumi ededlerin",tekreqemli_ededler*5,"faizidir")
      print("iki reqemli ededler umumi ededlerin",ikireqemli_ededler*5,"faizidir")
      print("üç reqemli ededler umumi ededlerin",ucreqemli_ededler*5,"faizidir")
faiz()