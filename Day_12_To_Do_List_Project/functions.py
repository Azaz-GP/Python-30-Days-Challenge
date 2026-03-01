from database import load_data,save_data
def add_task():
    data=load_data()
    task=input("Enter task: ")
    for de in data:
        if de["task"].lower()==task.lower():
            print("-----Task alreday added-----")
            return
    status="Pending" #by default
    priority=input("Enter task priority(High,Medium,Low): ")


    details={
        "task" : task,
        "status" : status,
        "priority":priority
    }
       
    data.append(details)
    print("Task Added")
    save_data(data)
def view_task():
    data=load_data()
    if not data:
        print("Not task added yet!")
        return
    print("Index  || Task || Status || Priority")
    for index,details in enumerate(data,start=1):
        print(f"{index}.Task: {details['task']}\nStatus: {details['status']}  Priority: {details['priority']}")
def comp_task():
    data=load_data()
    view_task()
    try:
        ind=int(input("Enter task index you complete: "))
        python_index=ind-1
        if python_index<0 or python_index>=len(data):
            print("Invaild index!")
            return
    except ValueError:
        print("Only numbers!")
        return
    data[python_index]["status"]="Complete"
    save_data(data)
def delete_task():
    data=load_data()
    view_task()
    try:
        ind=int(input("Enter task index you want to remove: "))
        python_index=ind-1
        if python_index<0 or python_index>=len(data):
            print("Invaild index!")
            return
    except ValueError:
        print("Only numbers!")
        return
    data.pop(python_index)
    save_data(data)
def edit_task():
    data=load_data()
    view_task()
    try:
        ind=int(input("Enter task index you edit: "))
        python_index=ind-1
        if python_index<0 or python_index>=len(data):
            print("Invaild index!")
            return
    except ValueError:
        print("Only numbers!")
        return
    new_task=input("Enter new task title: ")
    data[python_index]["task"]=new_task
    save_data(data)

def search_task():
    data=load_data()
    if not data:
        print("Not task added yet!")
        return
    ta=input("Enter task title you want to search: ")
    for details in data:
        if details["task"].lower()==ta.lower():
            print("Task founded!")
            print(f"Task: {details['task']}\nStatus: {details['status']}\nPriority: {details['priority']}")
            break