for num in range(100):
      if num%3==0:
            print(num)
"""tapsiriq 2"""
eded =int(input("ededi daxil edin: "))
for faktor in range(eded):
      faktor*=eded
print(faktor)
"""tapsiriq 3"""
say =int(input("neçə ədəd ulduz lazımdır? "))
print("*"*say,end="")
"""tapsiriq 4"""
print("\n")
for num in range(1,50):
      if num%2==0:
            print(num)
"""tapsiriq 5"""
min = int(input("diapozun ilk ededini daxil edin "))
max = int(input("diapozun son ededini daxil edin "))
cut_eded=0
tek_eded=1
if min>=max:
      print("ededleri düzgün daxil edin ")
for number in range(min,max):
      if number%2==0:
            cut_eded+=number
      elif (number-1)%2==0:
            tek_eded*=number
print(cut_eded)
print(tek_eded)