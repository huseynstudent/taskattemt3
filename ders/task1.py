name=" "
surname=" "
age=0
score=0.0
group=[]
while True:
      print("1-add student\n2-show students\n3-delete student\n0-exit")
      a=int(input(": "))
      if a==1:
            student=[]
            surname=str(input("input the surname: "))
            student.append(surname)            
            name=str(input("input the name: "))
            student.append(name)
            score=float(input("input the score: "))
            student.append(age)
            student.append(score)
            age=int(input("input the age: "))
            group.append(student)
            print(group)
      elif a==2:
            print(group)
      elif a==3:
            group.remove(student)
            print(group)
      elif a==0:
            break