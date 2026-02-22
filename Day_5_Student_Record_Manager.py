print("=====Student Record Manager")
student_dic={}
def add():
    global student_dic
    nam=input("Enter Student name: ")
    key=nam
    mak=int(input("Enter Student marks: "))
    value=mak
    student_dic[key]=value
def display():
    global student_dic
    if not student_dic:
     print("No students available")
     return
    for key,value in student_dic.items():
        print(f"{key} : {value}")
def update_marks():
    global student_dic
    na=input("Enter name of the Student whose number is need to update: ")
    key =na
    ma=int(input("Enter new marks: "))
    value=ma
    student_dic[key]=value
def del_student():
    global student_dic
    de=input("Enter name of the student for deleting: ")
    key=de
    if key in student_dic:
        del student_dic[key]
    else:
        print("Student not found")
def topper():

    top_key= None
    max_value=-1
    if not student_dic: # Check if dictionary is empty
        print("No students in the record yet!")
        return
    for key, value in student_dic.items():
        if value>max_value:
            max_value=value
            top_key=key
    print(f"The topper is {top_key} with {max_value} marks")

def menu():
    print("======Here are the Features======")
    while True:
        print("1.Add Student\n2.View all Student\n3.Update marks\n4.Delete student\n5.Show topper\n6.Exit")
        op=int(input("Choose Option: "))
        if op==1:
            add()
            print("==================\n")
        elif op==2:
            display()
            print("==================\n")
        elif op==3:
            update_marks()
            print("==================\n")
        elif op==4:
            del_student()
            print("==================\n")
        elif op==5:
            topper()
            print("==================\n")
        elif op==6:
            break
        else:
            print("Invalid option")
        
menu()
