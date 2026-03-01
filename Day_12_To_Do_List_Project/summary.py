from database import load_data
def all_summ():
    data=load_data()
    if not data:
        print("No Task added")
        return
    total_task=len(data)
    comp_task=0
    pen_task=0
    for details in data:
        if details['status']=='Complete':
            comp_task+=1
        elif details['status']=='Pending':
            pen_task+=1
    print(f"Total task: {total_task}\nCompleted Tasks: {comp_task}\nPending Task: {pen_task}")
def high_prio_pen():
    data=load_data()
    if not data:
        print("No Task added")
        return
    for details in data:
        if details["status"]=="Pending" and details["priority"].lower()=="High".lower():
            print(f"High Pirority Pending Task are: {details['task']}")
        
def pen_only():
    data=load_data()
    for details in data:
        if details['status']=='Pending':
            print(f"Pending Tasks: {details['task']}")