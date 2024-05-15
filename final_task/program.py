hamburgers_num=10
fries_num=15
coffee_num=10
water_bottles_num=30
hot_dogs_num=20
hamburgers=8
fries=3
hot_dogs=6
coffee=2
water_bottles=1
cost=0
def benzin(costs):
   global cost
   while True:
      dizel=0.6
      a92=0.9
      premium=1.15
      print("____________________________________________________________________________________________________________")
      benzin_novu=int(input("Hansı benzini itsəyirsiniz?\n1-dizel\n2-a92\n3-premium"))
      if benzin_novu==2:
            nov=a92
      elif benzin_novu==1:
            nov=dizel
      elif benzin_novu==3:
            nov=premium
      else:
           print("sehv nomre daxil edilib")
           continue
      print("____________________________________________________________________________________________________________")
      odenis=str(input("litrlə alacaqsınız, yoxsa qiymətə görə?"))
      if odenis.lower()=="litrle" or odenis.lower()=="litr" or odenis.lower()=="litrlə":
           ode=int(input("Neçə litr?"))
           continu=str(input(f"{round(ode*nov,2)}manat olacaq, almaq istəyirsiniz?"))
           if continu.lower()!="hə" or continu.lower()!="yes" or continu.lower()!="he":
            cost+=round(ode*nov,2)
            break
           else:
               break
      elif odenis.lower()=="qiymete gore" or odenis.lower()=="qiymet" or odenis.lower()=="qiymətə görə":
            ode=int(input("neçeye?"))
            print(f"cemi {int(ode//nov)} litr")
            cost+=ode
      else:
           print("səhv ödəniş üsulu daxil edilib")
           continue
print("\t","Best oil".center(30,"#"))
while True:
      print("Best oilə xoş gəlmisiniz")
      emeliyyat=int(input("1.benzin doldurmaq\n2.mini kafe\n3.ödəniş etmək"))
      if emeliyyat==1:
            benzin(1)
            print(cost)
      elif emeliyyat==2:
            print("____________________________________________________________________________________________________________")
            print("Mini-kafeyə xoş gəlmişsiniz,burada sizin üçün burgerlər(8 man),kartof frilər(3 man) və hot doqlar(6 man) hazırlanır.İstəsəniz yanında fincanda kofe(2 man) və ya plastik qabda(500 ml) su(1 man) ala bilərsiniz")
            while True:
                  food=str(input("Nə almaq istəyirsiniz?"))
                  if food.lower()=="burger" or food.lower()=="hamburger" or food.lower()=="qamburger":
                       choice=hamburgers_num
                       food_fee=hamburgers
                  elif food.lower()=="fri" or food.lower()=="kartof fri" or food.lower()=="frilər" or food.lower()=="kartof frilər":
                       choice=fries_num
                       food_fee=fries
                  elif food.lower()=="hot dog" or food.lower()=="hot dogs" or food.lower()=="hot doqlar" or food.lower()=="hot doqs" or food.lower()=="hot doq":
                       choice=hot_dogs_num
                       food_fee=hot_dogs
                  elif food.lower()=="kofe" or food.lower()=="coffee" or food.lower()=="fincanda kofe":
                       choice=coffee_num
                       food_fee=coffee
                  elif food.lower()=="su" or food.lower()=="butulkada su":
                       choice=water_bottles_num
                       food_fee=water_bottles
                  else:
                       continue
                  if choice==0 :
                       print("Üzr istəyirik.Bu məhsuldan stokda qalmayıb.")
                       continu=str(input("Başqa nə isə almaq istəyirsiniz?"))
                       if continu.lower()=="hə" or continu.lower()=="yes" or continu.lower()=="he":
                         continue
                       else:
                         break
                  count=int(input("Neçə dənə?"))
                  if count<=choice:
                        print(f"Qiymət: {food_fee*count}man")
                        cost+=food_fee*count
                        continu=str(input("Başqa nə isə almaq istəyirsiniz?"))
                        if continu.lower()=="hə" or continu.lower()=="yes" or continu.lower()=="he":
                            continue
                        else:
                            break
                  elif count>choice:
                       print("stokta o qeder qalmayib")
                       continue
      elif emeliyyat==3:
            print(f"sizin borcunuz {cost} manatdir")
            od_novu=str(input("kartla yoxsa nağd?"))
            if od_novu.lower()=="kartla" or od_novu.lower()=="kart":
                  kart=int(input("kartın nömrəsini daxil edin:"))
                  print("balans yetərli deyil,nağd ödəyin zəhmət olmasa   (￣_,￣ )")
                  leave=str(input("nağd ödəniş alınsın?(yes,no)"))
                  if leave.lower()=="no" or leave.lower()=="yox":
                       break
                  else:
                       print("Nağd ödəniş alındı.Gəldiyiniz üçün sağolun.Yenə gözləyərik!")
                       break
            elif od_novu.lower()=="nağd" or od_novu.lower()=="nağdla" or od_novu.lower()=="nagd" or od_novu.lower()=="nagdla":
             print("Gəldiyiniz üçün sağolun.Yenə gözləyərik!")
             break
            else:
                  print("yanlış emeliyyat daxil edilib")
      else:
            print("yanlış emeliyyat daxil edilib")