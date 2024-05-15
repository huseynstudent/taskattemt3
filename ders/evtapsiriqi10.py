eded=int(input("ededi daxil edin: "))
cemi=0
for i in range(1,eded+1):
      cemi+=i*i
print(cemi)
"""tapsiriq2"""
eded=int(input("ededi daxil edin: "))
for i in range(2):
      for j in range(eded):
            print("*",end="")
      print()
      for g in range((eded-3)//3):
            print("*",end="")
            for b in range(2):
                  for d in range((eded-3)//2):
                        print(" ",end="")
                  print("*",end="")      
            print()
for a in range(eded):
      print("*",end="")
