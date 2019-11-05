lst=[]
while(True):
    print("----------------Student Data Storage--------------------")
    print("1.Create New Student                2.Fetch Data")
    while(True):
      try:
       ask=int(input("Enter Command:"))
       if ask==0 or ask==1 or ask==2:
         break
       else:
          print("+.+.+.+.+.+.+.+.+.+.+.+Wrong Input.+.+.+.+.+.+.+.+.+.+.+.+")
          print("\n----------------Student Data Storage--------------------")
          print("1.Create New Student                2.Fetch Data")
      except Exception:
        print("+.+.+.+.+.+.+.+.+.+.+.+Wrong Input.+.+.+.+.+.+.+.+.+.+.+.+")
        print("\n----------------Student Data Storage--------------------")
        print("1.Create New Student                2.Fetch Data")
        continue
    if ask==0:
        break
    elif ask==1:
      try:
        num=int(input("Enter ID of Student:"))
        name=input("Enter Student Name:")
        age=int(input("Enter Age of {}:".format(name)))
        gen=input("Enter Gender of {}(M/F):".format(name))
        if gen=='M' or gen=='F':
          pass
        else:
          raise Exception
        stu=[num,name,age,gen]
        lst.append(stu)
        print("Student Data Stored...!!!")
      except Exception:
        print("+.+.+.+.+.+.+.+.+.+.+.+Wrong Input.+.+.+.+.+.+.+.+.+.+.+.+\n")
    elif ask==2:
      try:
        print("Fetch Data By ----> 1.ID Number  2.Name of Student")
        ask2=int(input("Enter Command:"))
        if ask2==1 or ask2==2:
          pass
        else:
          raise Exception
        if ask2==1:
          ask3=int(input("Enter Id of Student:"))
          for i in lst:
            if ask3==i[0]:
              print("Id:{}    Name:{}    Age:{}   Gender:{}".format(i[0],i[1],i[2],i[3]))
              break
          else:
            print("-------------------/Record NOT Found\-------------------")
        elif ask2==2:
          ask4=input("Enter Name of Student:")
          for j in lst:
            if j[1]==ask4:
              print("Id:{}    Name:{}    Age:{}   Gender:{}".format(j[0],j[1],j[2],j[3]))
              break
          else:
            print("-------------------/Record NOT Found\-------------------")
        else:
          pass
      except Exception:
        print("+.+.+.+.+.+.+.+.+.+.+.+Wrong Input.+.+.+.+.+.+.+.+.+.+.+.+\n")
    
