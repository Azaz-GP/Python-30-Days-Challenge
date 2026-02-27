import json
def load_data():
    try:
     with open("Password.json","r") as file:
        data=json.load(file)
        return data
    except:
       return []
def save_data(data):
      with open("Password.json","w") as file:
         json.dump(data,file,indent=4)
