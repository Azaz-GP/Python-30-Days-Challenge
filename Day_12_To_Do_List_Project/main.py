from functions import add_task, view_task, delete_task, comp_task, edit_task,search_task
from summary import all_summ,pen_only,high_prio_pen

def menu():
    print("====Welcome to ToDo List====")
    while True:
        print("\n====Tools====")
        print("1.Add Task\n2.View Task\n3.Delete Task\n4.Complete Task\n5.Edit Task\n6.Search Task\n7.Pending Task\n8.High Priority Pendings\n9.Full tasks summary\n10.Exist")
        print("=================")
        
        try:
            op = int(input("Enter your choice: "))
        except ValueError:
            print("Only numbers!")
            continue # This sends them back to the start of the loop to try again

        if op == 1:
            add_task()
        elif op == 2:
            view_task()
        elif op == 3:
            delete_task()
        elif op == 4:
            comp_task()
        elif op == 5:
            edit_task()
        elif op == 6:
           search_task()
        elif op==7:
            pen_only()
        elif op==8:
            high_prio_pen()
        elif op==9:
            all_summ()
        elif op==10:
         print("Goodbye!!!")
         break
        else:
            print("Invalid Choice!")

menu()