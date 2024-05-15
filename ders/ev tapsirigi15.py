import random
def esl_reqem():
      eded=int(input("ededi daxil edin: "))
      bolen=0
      for i in range(eded-1):
            if eded%(i+1)==0:
                  bolen+=i+1
      if bolen==eded:
            print("eded esl reqemdir")
      else:
            print("eded esl reqem deyil")
esl_reqem()
"""task2    kart verilmeyib"""
"""task3    alinmadi sildim"""
print("task4")
def xosbext_eded():
      eded=int(input("ededi daxil edin(en az 6reqemli olmalidir)"))
      eded=str(eded)
      if int(eded)<100001:
            print("eded 6- reqemlidir")
      else:
            ilk_eded=int(eded[0])
            ikinci_eded=int(eded[1])
            ucuncu_eded=int(eded[2])
            sonuncu_eded=int(eded[-1])
            son_ikinci_eded=int(eded[-2])
            son_ucuncu_eded=int(eded[-3])
            ilk_3=ilk_eded+ikinci_eded+ucuncu_eded
            son_3=sonuncu_eded+son_ikinci_eded+son_ucuncu_eded
            if ilk_3==son_3:
                  print("eded xosbext ededdir")
            else:
                  print("eded xosbext eded deyil")
xosbext_eded()
"""task5  alinmadi sildim"""
print("task6")
list=[]
for i in range(10):
    x=random.randint(0,100)
    list.append(x)
print(list)
def eded_orta(list):
    sum=0
    for j in list:
        sum+=j
    return sum/10
print(eded_orta(list))
print("task7")
def count(): 
      list=[]
      menfiler=0
      sifirlar=0
      musbet=0
      for j in range(10):
            x=random.randint(-10,10)
            list.append(x)
      print(list)
      for i in list:
            if i<0:
                  menfiler+=1
            elif i>0:
                  musbet+=1
            else:
                  sifirlar+=1
      print(menfiler,"eded menfi,",end="")
      print(musbet,"eded musbet,",end="")
      print(sifirlar,"eded 0 var")
count()
print("task8")
def muqayise(min,max):
      list=[]
      max=0
      min=100
      for j in range(10):
        x=random.randint(-100,100)
        list.append(x)
      print(list)
      for i in list:
        if i>max:
              max=i
        elif i<min:
              min=i
      return min,max
print(muqayise(min,max))
print("task9 butun ededleri eksi ile evez et")
def reverse():
      list=[]
      for j in range(10):
        x=random.randint(-100,100)
        list.append(x)
      print(list)
      for i in range(len(list)):
          list[i]*=-1
      print(list)
reverse()
print("task10")
list=[]
for i in range(10):
    x=random.randint(1,100)
    list.append(x)
print(list)
def sadeler():
      sade=0
      for i in list:
       bolunen=0
       for j in range(i+1):
            if i%(1+j)==0:
                bolunen+=1
       if bolunen==2:
            sade+=1
      return sade
print("sade ededlerin sayi:",sadeler())



print("ders2")

print("task1")
A=[]
for i in range(5):
    x=random.randint(0,10)
    A.append(x)
print(A)
B=[]
for i in range(5):
    x=random.randint(0,10)
    B.append(x)
print(B)
C=[]
def birlesdirme():
      for i in range(10):
        if i%2==0:
            C.append(A[i//2])
        else:
            C.append(B[i//2])
      print(C)
birlesdirme()
print("task2")
listim=[]
for i in range(5):
    x=random.randint(-4,4)
    listim.append(x)
print(listim)
list2=[]
def kopya():
      for i in listim:
        if i<0:
            list2.append(i)
      for i in listim:
        if i==0:
            list2.append(i)
      for i in listim:
        if i>0:
            list2.append(i)
      print(list2)
kopya()
print("task3")
A=[]
for i in range(5):
    x=random.randint(0,10)
    A.append(x)
print(A)
def sort():
      for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i]>A[j]:
                x=A[i]
                A[i]=A[j]
                A[j]=x
      print(A)
sort()
print("task4-5")
M=random.randint(5,10)
N=random.randint(5,10)
A=[]
B=[]
ortaq=[]
ayri=[]
for i in range(M):
    x=random.randint(0,10)
    A.append(x)
print(A)
for i in range(N):
    x=random.randint(0,10)
    B.append(x)
print(B)
def ortaqlar():
      for i in A:
        for j in B:
            if j==i and i not in ortaq:
                ortaq.append(i)
      print("iki listdede eyni olan ededler:",ortaq)
def ayrilar():
      for i in A:
        for j in B:
            if not i in ortaq and i not in ayri:
                ayri.append(i)
      print("ilk listde olub o birinde olmayan ededler:",ayri)
ortaqlar()
ayrilar()
""""""