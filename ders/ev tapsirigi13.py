"""tapsiriq1"""
telefon=["Samsung S5","Samsung S6","Samsung S7","SamsungS8"]
print(telefon)
"""tapsiriq2"""
print(len(telefon))
"""tapsiriq3"""
ilk=telefon[0]
son=telefon[-1]
print(ilk,son)
"""tapsiriq4"""
telefon[0] = "Samsung S9"
print(telefon)
"""tapsiriq5"""
a = telefon.count("Samsung S6")
if a>=1:
      print("yes")
else:
      print("No")
"""tapsiriq6"""
print(telefon[:2])
"""tapsiriq7"""
telefon[-2:] = ["Samsung S9" , "Samsung S10"]
print(telefon)
"""tapsiriq8"""
telefon.append("IPhone X")
telefon.append("IPhone XR")
print(telefon)
"""tapsiriq9"""
telefon.pop()
print(telefon)
"""tapsiriq10"""
telefon.reverse()
print(telefon)