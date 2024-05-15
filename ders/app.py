num=int(input("ededi daxil edin: "))
for i in range(num+1):
      for j in range(2*num):
            if j<num+i and j>num-i:
                  print("*",end="")
            else:
                  print(end=" ")
      print()
"""h1"""
num=int(input("ededi daxil edin: "))
for i in range(num):
      for j in range(num):
            if i==0 or i==num-1 or j==0 or j==num-1 or j<num//3-1 and i<num//3 or i>num-num//3 and j<num//3-1 or j>num-num//3 and i<num//3 or j>num-num//3 and i>num-num//3:
                  print("*",end="")
            else:
                  print(end=" ")
      print()
"""h2"""
num=int(input("ededi daxil edin: "))
for i in range(num):
      for j in range(num):
            if i==0 or i==num-1 or j==0 or j==num-1 or j==num//3-1 and i<num//3 or j<num//3-1 and i==num//3-1  or i==num-num//3 and j<num//3-1 or i>num-num//3-1 and j==num//3-1 or j==num-num//3 and i<num//3 or j>num-num//3 and i==num//3-1 or j==num-num//3 and i>num-num//3-1 or j>num-num//3 and i==num-num//3:
                  print("*",end="")
            else:
                  print(end=" ")
      print()
"""h7"""
num=int(input("ededi daxil edin: "))
for i in range(num):
      for j in range(num):
            if i==0 or i==num-1 or j==0 or j==num-1 or i==j or j==num-i-1:
                  print("*",end="")
            else:
                  print(end=" ")
      print()