import Pass5
import random
import time

path = "/Volumes/Key/"


def addPass(name, data, ID, IDOG):
    string = ""
    for info in data:
        string += info["name"] + "/" + info["user"] + "/" + info["password"] + "/" + info["notes"] + "\n"

    coded = Pass5.code(string, ID, IDOG)
    Pass5.openWrite(name, coded)


def genPass(length, include = "0"):
    new_pass = ""
    alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    num = ["1","2","3","4","5","6","7","8","9","0"]
    sign = ["!", "@", "#", "$", "%", "&", ",", ".", "-"]
    parts = []

    if "1" in include:
        parts += [alph]
    if "2" in include:
        parts += [num]
    if "3" in include:
        parts += [sign]
    if "1" not in include and "2" not in include and "3" not in include:
        parts = [alph, num, sign]

    for i in range(length):
        part = random.choice(parts)
        new_pass += random.choice(part)
    return new_pass


def recrypt():
    global path
    files = Pass5.openRead("files.txt")
    files = files.split("\n")


    ID = Pass5.openRead(path+"ID.txt")
    ID = ID.split("\n")
    del ID[-1]

    IDOG = Pass5.openRead(path+"IDOG.txt")
    IDOG = IDOG.split("\n")
    del IDOG[-1]


    Pass5.genIDPath(94, 94, path)
    nID = Pass5.openRead(path+"ID.txt")
    nID = nID.split("\n")
    del nID[-1]

    nIDOG = Pass5.openRead(path+"IDOG.txt")
    nIDOG = nIDOG.split("\n")
    del nIDOG[-1]
    
    for file in files:
        og = Pass5.openRead(file)
        decoded = Pass5.decode(og, ID, IDOG)
        new = Pass5.code(decoded, nID, nIDOG)
        Pass5.openWrite(file, new)

    last = Pass5.openRead("times.txt")
    last = last.split("\n")
    cur = str(time.time())
    new = last[0] + "\n" + cur
    Pass5.openWrite("times.txt", new)


def isTime():
    file = Pass5.openRead("times.txt")
    curTime = time.time()
    file = file.split("\n")
    every = float(file[0])
    lastTime = float(file[1])
    past = every * 86400
    if lastTime + past < curTime:
        return True
    else:
        return False

        

def main():
    global path

    if isTime():
        recrypt()
        print("Recrypt ran")
        print("---------------")
    
    while True:
        do = input("Enter: ")
        print()

        if do in ["pass", "passwords", "keepsafe", "safe"]:
            while True:
                name = input("Enter Safe Name: ") + ".txt"
                try:
                    file = Pass5.openRead(name)
                except:
                    print("No",name,"File")
                    continue
                else:
                    break

            ID = Pass5.openRead(path + "ID.txt")
            ID = ID.split("\n")
            del ID[-1]
            IDOG = Pass5.openRead(path + "IDOG.txt")
            IDOG = IDOG.split("\n")
            del IDOG[-1]
            

            print()
            print("-"*30)
            print(name, "Opened")
            print()
            data = []
            decoded = Pass5.decode(file, ID, IDOG)
            split = decoded.split("\n")
            del split[-1]
            for line in split:
                line_split = line.split("/")
                in_data = {}
                in_data["name"] = line_split[0]
                in_data["user"] = line_split[1]
                in_data["password"] = line_split[2]
                if len(line_split) > 4:
                    in_data["notes"] = ""
                    for i in range(3, len(line_split)):
                        if i == len(line_split) - 1:
                            in_data["notes"] += line_split[i]
                        else:
                            in_data["notes"] += line_split[i] + "/"
                else:
                    in_data["notes"] = line_split[3]

                data += [in_data]

            while True:
                doing = input("Enter: ")
                print()

                if doing in ["read all", "all", "open all", "list", "list all"]:
                    for info in data:
                        print(data.index(info) + 1, ". ", info["name"], sep="")

                elif doing in ["enter","see","open"]:
                    while True:
                        try:
                            num = int(input("Enter Record: "))
                            this = data[num-1]
                        except:
                            continue
                        else:
                            print()
                            break
                    for info in this:
                        print(str.capitalize(info) + ": " + this[info])

                elif doing in ["add", "new"]:
                    adding_name = input("Enter Name: ")
                    adding_user = input("Enter User: ")
                    adding_password = input("Enter Password: ")
                    if adding_password in ["rand","random","gen","gen random", "new"]:
                        while True:
                            try:
                                length = int(input("Enter Length: "))
                            except:
                                continue
                            else:
                                break
                        print("1 - For Letters")
                        print("2 - For Numbers")
                        print("3 - For Signs")
                        include = input("Enter Include: ")
                        adding_password = genPass(length, include)
                    adding_notes = input("Add Notes: ")
                    this_data = {}
                    this_data["name"] = adding_name
                    this_data["user"] = adding_user
                    this_data["password"] = adding_password
                    this_data["notes"] = adding_notes
                    data += [this_data]

                    addPass(name, data, ID, IDOG)

                elif doing in ["change", "re-do", "fix"]:
                    print()
                    while True:
                        try:
                            num = int(input("Enter Record: "))
                            this = data[num-1]
                        except:
                            continue
                        else:
                            break
                    adding_name = input("Enter Name: ")
                    adding_user = input("Enter User: ")
                    adding_password = input("Enter Password: ")
                    if adding_password in ["rand","random","gen","gen random", "new"]:
                        while True:
                            try:
                                length = int(input("Enter Length: "))
                            except:
                                continue
                            else:
                                break
                        print("1 - For Letters")
                        print("2 - For Numbers")
                        print("3 - For Signs")
                        include = input("Enter Include: ")
                        adding_password = genPass(length, include)
                    adding_notes = input("Add Notes: ")
                    this_new = {}
                    this_new["name"] = adding_name
                    this_new["user"] = adding_user
                    this_new["password"] = adding_password
                    this_new["notes"] = adding_notes
                    data[num-1] = this_new
                    
                    addPass(name, data, ID, IDOG)

                elif doing in ["remove", "delete", "del"]:
                    while True:
                        try:
                            num = int(input("Enter Record: "))
                            data[num - 1]
                            this = num - 1
                            print('Are you sure you want to delete "', data[this]["name"], '"', sep="")
                            confirm = input("Yes/No: ")
                            if confirm in ["Y", "y", "yes", "Yes"]:
                                del data[this]
                                addPass(name, data, ID, IDOG)
                                break
                            elif confirm in ["N", "n", "no", "No"]:
                                break
                            else:
                                continue
                        except:
                            continue
                    
                    

                elif doing in ["help"]:
                    print("read all, all, open all, list, list all --> Lists all records")
                    print("enter, see, open                        --> Opens a record by their number")
                    print("add, new                                --> Creates a new record")
                    print("change, re-do, fix                      --> Re-writes an existing record")
                    print("remove, delete, del                     --> Deletes an existing record")
                    print("end, finish, done                       --> Closes the Safe")
                elif doing in ["end", "finish", "done"]:
                    print("-" * 30)
                    break

                print()


        
        elif do in ["open", "read"]:
            while True:
                try:
                    name = input("Enter File Name: ") + ".txt"
                    file = Pass5.openRead(name)
                except:
                    print("No", name, "File")
                    continue
                else:
                    break
            ID = Pass5.openRead(path + "ID.txt")
            ID = ID.split("\n")
            del ID[-1]
            IDOG = Pass5.openRead(path + "IDOG.txt")
            IDOG = IDOG.split("\n")
            del IDOG[-1]

            print(Pass5.decode(file, ID, IDOG))
                    
            
        elif do in ["recrypt", "change", "ID"]:
            recrypt()


        elif do in ["timer", "set timer", "timer set"]:
            while True:
                try:
                    every = input("Enter Timer: ")
                    every = float(every)
                    if every < 0 or every > 30:
                        continue
                except:
                    if "mins" in every:
                        every = every.replace("mins","")
                        every = every.replace(" ","")
                        try:
                            every = float(every)
                        except:
                            print("Invalid Entry")
                            continue
                        else:
                            every = every / 24 / 60
                            break
                    elif "hours" in every:
                        every = every.replace("hours","")
                        every = every.replace(" ","")
                        try:
                            every = float(every)
                        except:
                            print("Invalid Entry")
                            continue
                        else:
                            every = every / 24
                            break
                    print("Invalid Entry")
                else:
                    break
            every = str(every)
            cur = str(time.time())
            Pass5.openWrite("times.txt", every + "\n" + cur)

        
        elif do in ["help"]:
            print("pass, passwords, keepsafe, safe --> Opens a specific keepsafe file")
            print("open, read                      --> Opens and reads a specific file")
            print("make, write        (WIP)        --> Creates and writes a new file")
            print("recrypt, change, ID             --> Changes the enryption ID for all files")
            print("timer, set timer, timer set     --> Changes the timer for auto recryption")
            print("end, finish, done               --> Ends the program")
        
        elif do in ["end", "finish", "done"]:
            break

        print()
                    
                        
            
            
            
main()






