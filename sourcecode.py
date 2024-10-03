import pickledb
import rich
from rich.console import Console
from rich.text import Text
from rich import print
from rich.panel import Panel
import os
clear = lambda: os.system('cls')
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
                p = input("Choose password:")
                mai = input("Enter mailbox name ({name}@rmail.sdb):")
                mail = mai + '@rmail.sdb'
                db.set('m>' + u, mail)
                db.lcreate(mail)
                db.lcreate(mail + "<out")
                db.set(u, p)
                db.lcreate(ul)
                clear()
                break
    if login == "L":
        while True:
            if op == True:
                break
            qwe = input("Admin? Y or N :")
            ue = input("Username:")
            if qwe == "Y":
                checke = db.exists("u>" + ue + "<a")
            else:
                checke = db.exists("u>" + ue)
            if checke == True:
                if qwe == "Y":
                    u = "u>" + ue + "<a"
                else:
                    u = "u>" + ue
                pe = input("Password:")
                if qwe == "Y":
                    checkp = db.get("u>" + ue + "<a")
                else:
                    checkp = db.get("u>" + ue)
                if pe != checkp:
                    print("Wrong password")
                    clear()
                    continue
                else:
                    if qwe == "Y":
                        canDel = True
                    clear()
                    while True:
                        print("Welcome %s!" % ue)
                        action = input("N - new file, R - read file,\n L - list files , Q - to log out,\nS - for settings, M - for Rmail\n>")
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
                        if action == "M":
                            while True:
                                print("Rmail 1.0\nN - new letter|R - out|F - in|! - quit")
                                mail1 = db.get('m>' + u)
                                print(mail1)
                                dig = input('>')
                                if dig == "N":
                                    tema = input('Enter name:')
                                    if tema == "/quit":
                                        print('Wrong name.')
                                        continue
                                    komu = input('To:')
                                    if not db.exists(komu):
                                        print('No such mailbox.')
                                        continue
                                    text = input('')
                                    text = text + f'\nBy {mail1}'
                                    db.set(tema, text)
                                    db.ladd(komu, tema)
                                    db.ladd(mail1 + "<out", tema)
                                if dig == "R":
                                    print('/quit to quit')
                                    print(Panel(str(db.lgetall(mail1 + '<out')), title="All out"))
                                    search = input('Search:')
                                    if search == '/quit':
                                        continue
                                    if db.lexists(mail1 + '<out', search):
                                        print(f'Name:{search}\n{db.get(search)}')
                                    else:
                                        print("Not found.")
                                        continue
                                if dig == "F":
                                    print('/quit to quit')
                                    print(Panel(str(db.lgetall(mail1)), title="All in"))
                                    search = input('Search:')
                                    if search == '/quit':
                                        continue
                                    if db.lexists(mail1, search):
                                        print(f'Name:{search}\n{db.get(search)}')
                                    else:
                                        print("Not found.")
                                        continue
                                if dig == "!":
                                    break
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
                                    if qwe != "Y":
                                        canDel = db.lexists(ue, y)
                                    if canDel == True:
                                        fks = input("D to delete:")
                                        if fks == "D":
                                            fdel1 = db.lgetall("pubfiles").index(door)
                                            db.lpop("pubfiles", fdel1)
                                            db.rem(door)
                                            clear()
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
                            if qwe == "Y":
                                console.print("P - change password, [bold red]D - Delete other admin[/bold red], [blue]A - Create Admin user[/blue], ! for exit.")
                            else:
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
                                if qwe == "Y":
                                    xcv = input("Admin username:")
                                    checkau = db.exists(xcv)
                                    if checkau != True:
                                        print("Wrong username")
                                        continue
                                    xcvb = "u>" + xcv + "<a"
                                    hz = input("Are you sure? Y/N?")
                                    if hz == "Y":
                                        db.rem(xcvb)
                                        db.lremlist(xcv)
                                        db.lremlist(db.get('m>' + xcv))
                                        db.lremlist(db.get('m>' + xcv) + '<out')
                                        db.rem('m>' + xcv)
                                        continue
                                    
                                hz = input("Are you sure? Y/N?")
                                if hz == "Y":
                                    db.rem(u)
                                    db.lremlist(ue)
                                    db.lremlist(db.get('m>' + u))
                                    db.lremlist(db.get('m>' + u) + '<out')
                                    db.rem('m>' + u)
                                    op = True
                                    break
                            if qwe == "Y":
                                if jpke == "A":
                                    while True:
                                        ul = input("Choose username:")
                                        u = "u>" + ul + "<a"
                                        checkU = db.exists(u)
                                        if checkU == True:
                                            print("Username already taken")
                                            continue
                                        else:
                                            p = input("Choose password:")
                                            mai = input("Enter mailbox name ({name}@rmail.sdb):")
                                            mail = mai + '@rmail.sdb'
                                            db.set('m>' + u, mail)
                                            db.lcreate(mail)
                                            db.lcreate(mail + "<out")
                                            db.set(u, p)
                                            db.lcreate(ul)
                                            clear()
                                            break
                            if jpke == "!":
                                continue
            else:
                print("Wrong username")
                continue
    if login == "!":
        break
        
    
