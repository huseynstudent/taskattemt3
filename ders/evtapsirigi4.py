mil = int(input("mili daxil edin "))
km = 1.609*mil
print(km)
""" tapsiriq2 """
mesafe = int(input(" məsafəni km ilə daxil edin "))
vaxt = int(input("məsafəni qət etmə müddədini saat ilə daxil edin "))
sürət = mesafe/vaxt
print("saatda ",sürət,"kilometr sürətlə hərəkət edirdin")
"""tapsiriq3"""
N = int(input("ədədi daxil edin "))
F = int(input("faizi daxil edin "))
cavab = N*F/100
print(N, "ədədinin", F ,"faizi",cavab,"edir")
"""tapsiriq4"""
uz = int(input("Çevrənin uzunluğunu daxil edin "))
diametr = uz/3.14
print("diametr =",diametr)
"""tapsiriq5"""
R1 = int(input("R1 müqavimətini verin "))
R2 = int(input("R2 müqavimətini verin "))
R3 = int(input("R3 müqavimətini verin "))
a = 1/R1+1/R2+1/R3
R0 = 1/a
print(R0)