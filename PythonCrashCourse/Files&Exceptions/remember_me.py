from pathlib import Path
import json

path = Path('username.json')

def greet_user():
    mydict = fetch_data()
    if mydict:
        print(f"I know you! Your name is {mydict['name']}, you are {mydict['age']} years old and your favorite pokemon is {mydict['pokemon']}!")
    else:
        mydict = change_data()
        print(f"I will remember you, {mydict['name']}!")

def fetch_data():
    if path.exists():
        contents = path.read_text()
        mydict = json.loads(contents)
        return mydict
    else:
        return None

def change_data():
    username = input("What is your name?\t").title()
    age = input("How old are you?\t")
    poke = input("What is your favorite pokemon? Be honest!\t").title()
    mydict = {'name':username, 'age':age, 'pokemon':poke}
    contents = json.dumps(mydict)
    path.write_text(contents)
    return mydict

def delete_data():
    if path.exists():
        path.unlink()
        print(f"{path} deleted.")
    else:
        print(f"Path {path} cannot be deleted, because it does not exist.")
