hamburgers = 10
tester = 0
fries = 15
coffee = 10
water_bottles = 30
hot_dogs = 20
fee = 0
fixed_cost = 1000000  # Set your initial fixed cost here

def benzin(costs):
    cost = 0
    while True:
        a92 = 0.9
        premium = 1.15
        dizel = 0.6
        print("____________________________________________________________________________________________________________")
        benzin_novu = int(input("Hansı benzini itsəyirsiniz?\n1-dizel\n2-a92\n3-premium"))
        if benzin_novu == 2:
            nov = a92
        elif benzin_novu == 1:
            nov = dizel
        elif benzin_novu == 3:
            nov = premium
        else:
            print("sehv nomre daxil edilib")
            continue
        print("____________________________________________________________________________________________________________")
        odenis = str(input("litrlə alacaqsınız, yoxsa qiymətə görə?"))
        if odenis.lower() == "litrle" or odenis.lower() == "litr" or odenis.lower() == "litrlə":
            ode = int(input("Neçə litr?"))
            cost += ode * nov
            return ode * nov
        elif odenis.lower() == "qiymete gore" or odenis.lower() == "qiymet" or odenis.lower() == "qiymətə görə":
            ode = int(input("neçeye?"))
            print(f"cemi {int(ode // nov)} litr")
            cost += ode
            return ode
        else:
            print("səhv ödəniş üsulu daxil edilib")
            continue
    fee += cost

def display_receipt():
    print("Recept".center(50, "="))
    print(f"Fuel Cost: {fee} manat")
    print(f"Fixed Cost: {fixed_cost} manat")
    total_cost = fee + fixed_cost
    print(f"Total Cost: {total_cost} manat")
    print("=" * 50)

print("\t", "Best oil".center(30, "#"))

while True:
    print("Best oilə xoş gəlmisiniz")
    emeliyyat = int(input("1.benzin doldurmaq\n2.mini kafe\n3.ödəniş etmək"))
    
    if emeliyyat == 1:
        benzin(1)
        print(fee)  # cost gorunmur
    # elif emeliyyat == 2:

    elif emeliyyat == 3:
        print(f"sizin borcunuz {fee} manatdir")
        od_novu = str(input("kartla yoxsa nağd?"))
        
        if od_novu.lower() == "kartla" or od_novu.lower() == "kart":
            kart = int(input("kartın nömrəsini daxil edin:"))
            print("balans yetərli deyil,nağd ödəyin zəhmət olmasa   (￣_,￣ )")
            leave = str(input("nağd ödəniş alınsın?(yes,no)"))
            
            if leave.lower() == "no" or leave.lower() == "yox":
                break
            else:
                print("Nağd ödəniş alındı.Gəldiyiniz üçün sağolun.Yenə gözləyərik!")
                display_receipt()  # Display detailed receipt
                break
                
        elif od_novu.lower() == "nağd" or od_novu.lower() == "nağdla" or od_novu.lower() == "nagd" or od_novu.lower() == "nagdla":
            print("Gəldiyiniz üçün sağolun.Yenə gözləyərik!")
            display_receipt()  # Display detailed receipt
            break
            
        else:
            print("yanlış emeliyyat daxil edilib")

    else:
        print("yanlış emeliyyat daxil edilib")