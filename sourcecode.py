import pickledb
import rich
from rich.console import Console
from rich.text import Text
from rich import print
from rich.panel import Panel

console = Console()
while True:
    db = pickledb.load('db.db', True)
    op = False
    print("Choose: N sign up, L for log in, ! to exit")
    login = input("Choose:")
    if login == "N":
        while True:
            ul = input("Choose a username:")
            u = "u>" + ul
            checkU = db.exists(u)
            if checkU == True:
                print("Username is already exist")
                continue
            else:
                p = input("Choose password")
                db.set(u, p)
                db.lcreate(ul)
                break
    if login == "L":
        while True:
            if op == True:
                break
            ue = input("Username:")
            checke = db.exists("u>" + ue)
            if checke == True:
                pe = input("Password:")
                checkp = db.get("u>" + ue)
                if pe != checkp:
                    print("Wrong password")
                    continue
                else:
                    while True:
                        print("Welcome %s!" % ue)
                        action = input("N - new file, R - read file,\n L - list files , Q - to log out,\nS - for settings\n>")
                        if action == "N":
                            typef = input("P - for public, L - for private, ! for exit:")
                            if typef == "L":
                                    title = input("Title:")
                                    if title == "pubfiles":
                                        print("Title is incorrect.")
                                        continue
                                    else:
                                        content = input("")
                                        try:
                                            db.set(title, content)
                                            db.ladd(ue, title)
                                            continue
                                        except:
                                            continue
                            if typef == "P":
                                while True:
                                    title = input("Title:")
                                    if title == "pubfiles":
                                        print("Title is incorrect.")
                                        continue
                                    else:
                                        content = input("")
                                        content = content + " By " + ue
                                        try:
                                            db.set(title, content)
                                            db.ladd("pubfiles", title)
                                            break
                                        except:
                                            continue
                            else:
                                continue
                        if action == "R":
                            kup = input("P - public files, L - private files, ! for exit:")
                            if kup == "P":
                                door = input("Title:")
                                y = db.lexists("pubfiles", door)
                                if y == True:
                                    try:
                                        look1 = db.get(door)
                                    except:
                                        continue
                                    console.print(look1)
                                else:
                                    print("File not found")
                            elif kup == "L":
                                dur = input("Title:")
                                q = db.lexists(ue, dur)
                                if q == True:
                                    try:
                                        look6 = db.get(dur)
                                    except:
                                        print("")
                                    console.print(look6)
                                    hdsa = input("D to delete:")
                                    if hdsa == "D":
                                        db.rem(dur)
                                        db.lremvalue(ue, dur)
                                        continue
                                else:
                                    print("File not found")
                            elif kup == "!":
                                continue
                            else:
                                continue 
                        if action == "L":
                                print(Panel(str(db.lgetall("pubfiles")), title="All Public Files"))
                                print(Panel(str(db.lgetall(ue)), title="All Private Files"))
                        if action == "Q":
                            op = True
                            break
                        if action == "S":
                            console.print("P - change password, [bold red]D - Delete user[/bold red], ! for exit.")
                            jpke = input(">")
                            if jpke == "P":
                                nm = input("Password:")
                                gjg = db.get(u)
                                if nm != gjg:
                                    print("Invalid password")
                                    continue
                                else:
                                    mn = input("New password:")
                                    db.rem(u)
                                    db.set(u, mn)
                                    continue
                            if jpke == "D":
                                hz = input("Are you sure? Y/N?")
                                if hz == "Y":
                                    db.rem(u)
                                    db.lremlist(ue)
                                    op = True
                                    break
                            if jpke == "!":
                                continue
            else:
                print("Wrong username")
                continue
    if login == "!":
        break
        
    
