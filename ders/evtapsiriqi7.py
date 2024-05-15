man = int(input("məbləğı manatla daxil edin  "))
op = int(input("çevirmək istədiyiniz pul vahidini qeyd edin : \n1-avro\n2-dollar\n3-rubl"))
if op==1:
      print(man*0.54)
elif op==2:
      print(man*0.59)
elif op==3:
      print(man*52.12)
else:
      print("doğru operator daxil edin")
"""tapsiriq2"""
qiymet = int(input("malın kiloluq qiymetini secin qiyməti daxil edin "))
qram = int(input("qrami daxil edin "))
if qram<0:
      print("qramı yanlış daxil etmisiniz")
elif 0<qram<=100:
      print("endirim yoxdur")
elif 100<qram<=200:
      print(qiymet/10000*3*qram)
elif 200<qram<=300:
      print(qiymet/10000*5*qram)
elif 300<qram:
      print(qiymet/10000*7*qram)
"""tapsiriq3"""
"""bu tapsiriqin 2 nov helli var 1cisi"""
mexrec = int(input("Kəsrin məxrəcini daxil edin  "))
suret = int(input("Kəsrin sürətini daxil edin  "))
if suret>=mexrec:
      print("bu ədədin kəsr hissəsi var ")
else:
      print("bu ədədin kəsr hissəsi yoxdur ")    
"""hell yolu 2:(onluq kesr ucun )"""
kesr = int(input("kesri daxil edin  "))
if kesr>=1:
      print("bu ədədin kəsr hissəsi var ")
else:
      print("bu ədədin kəsr hissəsi yoxdur ")  
"""tapsiriq4"""
saat = int(input("saatı daxil edin:  "))
deqiqe = int(input("deqiqeni daxil edin:  "))
if 24<=saat or saat<0:
      print("saadı yanlış daxil etmisiniz")
elif 60<deqiqe or deqiqe<0:
      print("deqiqeni yanlış daxil etmisiniz")
"""tapsiriq5"""
ay = int(input("Neçənci ayda doğulmusunuz? "))
gun = int(input("Neçənci günündə?"))
if ay==1 and 22<=gun<=31:
      print("Oğlaq bürcüsünüz")
elif ay==12 and 1<=gun<=19:
      print("Oğlaq bürcüsünüz") #true
elif ay==1 and 20<=gun<=31:
      print("Dolça bürcüsünüz")
elif ay==2 and 1<=gun<=18:
      print("Dolça bürcüsünüz") #true
elif ay==2 and 19<=gun<=29:
      print("Balıqlar bürcüsünüz")
elif ay==3 and 1<=gun<=19:
      print("Balıqlar bürcüsünüz")
elif ay==3 and 21<=gun<=31:
      print("Qoç bürcüsünüz")
elif ay==4 and 1<=gun<=19:
      print("Qoç bürcüsünüz")
elif ay==4 and 20<=gun<=30:
      print("Buğa bürcüsünüz")
elif ay==5 and 1<=gun<=20:
      print("Buğa bürcüsünüz")
elif ay==5 and 21<=gun<=31:
      print("Əkizlər bürcüsünüz")
elif ay==6 and 1<=gun<=21:
      print("Əkizlər bürcüsünüz")
elif ay==6 and 21<=gun<=30:
      print("Xərçəng bürcüsünüz")
elif ay==7 and 1<=gun<=23:
      print("Xərçəng bürcüsünüz")
elif ay==7 and 23<=gun<=31:
      print("Şir bürcüsünüz")
elif ay==8 and 1<=gun<=23:
      print("Şir bürcüsünüz")
elif ay==8 and 23<=gun<=31:
      print("Qız bürcüsünüz")
elif ay==9 and 1<=gun<=23:
      print("Qız bürcüsünüz")
elif ay==9 and 23<=gun<=30:
      print("Tərəzi bürcüsünüz")
elif ay==10 and 1<=gun<=22:
      print("Tərəzi bürcüsünüz")
elif ay==10 and 23<=gun<=31:
      print("Əqrəb bürcüsünüz")
elif ay==11 and 1<=gun<=21:
      print("Əqrəb bürcüsünüz")
elif ay==11 and 22<=gun<=30:
      print("Oxatan bürcüsünüz")
elif ay==12 and 1<=gun<=21:
      print("Oxatan bürcüsünüz")
else:
      print("ayı və ya günü yanlış daxil etmisiniz")
