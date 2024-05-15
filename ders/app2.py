name=0
surname=0
age=0
score=0
group=[]
while True:
      print("1-add student")
      print("2-show students")
      print("3-delete student")
      operator=int(input("0-exit: "))
      if operator==1:
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
      elif operator==2:
            print(group)
      elif operator==3:
            group.remove(student)
            print(group)
      elif operator==0:
            break