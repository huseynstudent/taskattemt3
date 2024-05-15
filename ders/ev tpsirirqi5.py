X = int(input("ilk ədədi daxil edin "))
Y = int(input("ikinci ədədi daxil edin "))
if X%Y :
      print("Yes")
else:
      print("No")
"""tapsiriq2"""
eded = int(input(" ədədi daxil edin "))
if eded%3:
      print("bu ədəd 3-ə qalıqsız bölünür")
else:
      print("bu ədəd 3-ə qalıqsız bölünmür")
if eded%5:
      print("bu ədəd 3-ə qalıqsız bölünür")
else:
      print("bu ədəd 3-ə qalıqsız bölünmür")
if eded%7:
      print("bu ədəd 3-ə qalıqsız bölünür")
else:
       print("bu ədəd 3-ə qalıqsız bölünmür")
"""tapsiriq3"""
eded = float(input(" ədədi daxil edin "))
if eded<0:
       print(eded*-1)
else:
       print(eded)
"""tapsiriq4"""
eded = int(input(" ədədi daxil edin "))
if eded<0:
       print("eded menfidir")
elif eded==0:
       print("bu eded 0-dır")
elif 0<eded<10:
       print("bu eded 1 reqemlidir")
elif 10<=eded<100:
       print("bu eded 2 reqemlidir")
elif 100<=eded<1000:
       print("bu eded 3 reqemlidir")
elif 1000<=eded<10000:
       print("bu eded 4 reqemlidir")
"""tapsiriq5     eleye bilmedim"""
# eded = int(input(" 5 rəqəmli ədədi daxil edin "))
# print(eded/1000%100)
# print(eded%100/10)
# """bura 5 rəqəmli ədəd oldugunu testiqleme qoyacam"""
# if 10000<=eded<100000:
#       print("   ")
# else:
#       print("5rəqəqmli ədəd daxil edin")
# if eded/1000==eded%100 :
#       print("bu eded polidromdur")
# else:
#       print("bu eded polidrom deyil")
"""tapsiriq6"""
code="sleep"
answer=str(input("enter the code "))
print("hint:something programmers love but rarely get enough  :)")
if answer == code:
      print("Access succesfully completed  ")
else:
      print("Acces denied")
