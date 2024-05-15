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
"""h3"""
num=int(input("ededi daxil edin: "))
for i in range(num//2):
      for j in range(num):
            if i>=j and j<num//2 or j==num//2 or j>num//2 and j>=num-i-1:
                  print("*",end="")
            else:
                  print(end=" ")
      print()
for i in range(num//2,1,-1):
      for j in range(num,0,-1):
            if i>=j+1 and j<=num//2 or j==num//2+1 or j>num//2 and j>=num-i+2:
                  print("*",end="")
            else:
                  print(end=" ")
      print()
# """h4"""
num=int(input("ededi daxil edin: "))
for i in range(num//2+2):
      for j in range(num):
            if j<num//2+i and j>num//2-i:
                  print("*",end="")
            else:
                  print(end=" ")
      print()
for i in range(num//2,0,-1):
      for j in range(num,0,-1):
            if j<num//2+i+1 and j>num//2-i+1:
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
"""h4"""
num=int(input("ededi daxil edin: "))
for i in range(num+1):
      for j in range(2*num):
            if j<num+i and j>num-i:
                  print("*",end="")
            else:
                  print(end=" ")
      print()
"""h5"""
num=int(input("ededi daxil edin: "))
for i in range(num//2):
      for j in range(num):
            if j==num//2+i or j==num//2-i:
                  print("*",end="")
            else:
                  print(end=" ")
      print()
for i in range(num//2+1,0,-1):
      for j in range(num,0,-1):
            if j==num//2+i+1 or j==num//2-i+1:
                  print("*",end="")
            else:
                  print(end=" ")
      print()