import json 
def load_data():
    try:
        with open("marks.json","r") as file:
            data=json.load(file)
            return data
    except FileNotFoundError:
        #file doesn't existed
        return []
    except json.JSONDecodeError:
        #file exists but empty or corrupted
        return []
def save_data(data):
   with open("marks.json","w") as file:
      json.dump(data,file,indent=4)
def add_student():
   data=load_data()
   while True:
     try:
      roll_no=int(input("Enter Roll No: "))
      break
     except:
        print("only integers")
        return
   while True:
      try:
        marks=int(input("Enter marks: "))
        break
      except:
        print("Only Integers")
        return
   student={
      "roll_no": roll_no,"marks": marks}
   for s in data:
    if s["roll_no"] == roll_no:
        print("Student already exists")
        return
   data.append(student)
   save_data(data)
def view_data():
   data=load_data()
   if not data:   #this will check list is empty
      print("No student records found.")
      return
   print("\n===== Student Records =====")
   for index,student in enumerate(data,start=1):
        roll_no = student["roll_no"]
        marks = student["marks"]
     # Step 5: Check pass/fail
        if marks >= 50:
            status = "Pass"
        else:
            status = "Fail"

        # Step 6: Print formatted output
        print(f"{index}. Roll No: {roll_no} | Marks: {marks} | Status: {status}")

    # Step 7: confirmation
   print("\nAll records displayed successfully.")





