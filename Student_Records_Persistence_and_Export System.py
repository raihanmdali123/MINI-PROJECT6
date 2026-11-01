import json
import csv
from datetime import datetime
print("==========STUDENT REPORT==========")
students=[]


def add():
    no =int(input("enter no. of student to add: "))
    for i in range(no):
        name = input("enter student's name:")
        rollno = int(input("enter  student's roll no. : "))

        with open("student.json","r") as file:
             data = json.load(file)

        for roll  in data:
             if rollno == roll["rollno"]:
             
                print("roll no exist:\n" \
                "please try unique roll no.  ")
        
             

        marks=[]
        for i in range(6):
            if i==1:
                mark= int(input("enter marks of python: "))
                marks.append(mark)
            elif i==2:
                mark = int(input("enter mark of DBMS: "))
                marks.append(mark)
            elif i==3:
                mark= int(input("enter marks of OS: "))
                marks.append(mark)
            elif i==4:
                            mark= int(input("enter marks of math: "))
                            marks.append(mark)
            elif i==5:
                            mark= int(input("enter marks of CN: "))
                            marks.append(mark)

        student={
           "name":name,
           "rollno":rollno,
           "marks":marks
        }
        students.append(student)
    with open("student.json", "w") as file:
           json.dump(students,file,indent=3)
    print("STUDENT ADDED SUCCESSFULLY")
def display():
       print("====list of student====")
       with open("student.json","r") as file:
          studentdata = json.load(file)      
       for student in studentdata:
                
            print("name:",student["name"])
            print("Roll No.: ",student["rollno"])
            for i in range(0,len(student["marks"])):
                if i==0:
                      print("PYTHON: ",student["marks"][i])
                if i==1:
                      print("DBMS:    ",student["marks"][i])
                if i==2:
                      print("OS:      ",student["marks"][i])
                if i==3:
                      print("MATH:    ",student["marks"][i])
                if i==4:
                      print("CN:      ",student["marks"][i])

       

def search():

    searchrollno=int(input("enter roll no of student to search: "))
    with open("student.json", "r") as file:
            data = json.load(file)
    for student in data:
          if searchrollno == student["rollno"]:
                print("name:",student["name"])
                print("Roll No.: ",student["rollno"])
                for i in range(0,len(student["marks"])):
                    if i==0:
                        print("PYTHON: ",student["marks"][i])
                    if i==1:
                        print("DBMS:    ",student["marks"][i])
                    if i==2:
                        print("OS:      ",student["marks"][i])
                    if i==3:
                        print("MATH:    ",student["marks"][i])
                    if i==4:
                        print("CN:      ",student["marks"][i])
def result():

    searchrollno=int(input("enter roll no of student to search: "))
    with open("student.json", "r") as file:
            data = json.load(file)
    for student in data:
          if searchrollno == student["rollno"]:
                print("name:",student["name"])
                print("Roll No.: ",student["rollno"])
                total = 0
                for i in range(0,len(student["marks"])):
                    total = total + student["marks"][i]

                    if i==0:
                        print("PYTHON: ",student["marks"][i])
                    if i==1:
                        print("DBMS:    ",student["marks"][i])
                    if i==2:
                        print("OS:      ",student["marks"][i])
                    if i==3:
                        print("MATH:    ",student["marks"][i])
                    if i==4:
                        print("CN:      ",student["marks"][i])

                print("TOTAL: ", total)
                percent=total
                print("PERCENTAGE: ",percent,"%")
                if percent>=80:
                  print("GRADE :A")
                elif percent>=60:
                     print("GRADE :B")
                elif percent>=40:
                     print("GRADE :C")
                else:
                     print("FAIL")

def topper():
    with open("student.json", "r") as file:
            data = json.load(file)
    highest= 0
    toppername = "none"
    for student in data:
         if sum(student["marks"])> highest:
              highest=sum(student["marks"])
              toppername  = student["name"]
    print("TOPPER IS: ", toppername)
    print("TOTAL MARKS IS; ",highest)
def classst():
    with open("student.json", "r") as file:
        data = json.load(file)
    total = 0
    for i in data:
        total   += 1
    print("total student",total)
    totalmark=0
    highest =0
    lowest =100
    passed =0
    fail=0

    for mark in data:
        
        if highest<(sum(mark["marks"])):
            highest = (sum(mark["marks"]))
        if lowest>(sum(mark["marks"])):
             lowest=  sum(mark["marks"])

         
        totalmark += sum(mark["marks"])
        if sum(mark["marks"])>40:
             
             passed+=1
        else:
             fail+=1
             
    print( "class average" ,totalmark/len(data))
    print("highest: ",highest,"%")
    print("lowest",lowest,"%")
    topper()
    print("student passed",passed)
    print("student fail",fail)


def logactivity(message):
    with open("activity_log.txt","a") as file:
        time =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(time + " - " + message + "\n")

def export_csv():
    with open("student.json","r") as file:
        data = json.load(file)

    with open("students.csv","w",newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Student ID","Name","Department",
            "Python","DBMS","OS","Math","CN"
        ])

        for student in data:
            writer.writerow([
                student["rollno"],
                student["name"],
                student.get("department","CSE"),
                student["marks"][0],
                student["marks"][1],
                student["marks"][2],
                
            ])

    logactivity("Students exported to students.csv")
    print("STUDENTS EXPORTED SUCCESSFULLY")
    

while True:
    print(
          "1.Add student\n" 
          "2.Display student\n" 
          "3.Search student\n" 
          "4.Student result\n" 
          "5.Find topper\n" 
          "6.Class statistic\n" 
          "7.Export CSV"
          "8.Exit"
     )
    ch = int(input("enter your choice: "))
    if ch==1:
          add()
    elif ch==2:
         display()
    elif ch == 3:
         search()
    elif ch == 4:
         result()
    elif ch == 5:
         topper()
    elif ch ==6:
         classst()
    elif ch == 7:
         export_csv()
    elif ch==8:
        print("===thank you===")
        break
    else:
         print("invalid choice")