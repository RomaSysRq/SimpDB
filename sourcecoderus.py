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
    print("Выберете: N - зарегестрироватся, L - войти, ! - выход")
    login = input("Выберете:")
    if login == "N":
        while True:
            ul = input("Выберете имя:")
            u = "u>" + ul
            checkU = db.exists(u)
            if checkU == True:
                print("Имя занято")
                continue
            else:
                p = input("Выберете пароль:")
                mai = input("Введите название почтового ящика ({название}@rmail.sdb):")
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
            qwe = input("Администратор? Д or Н :")
            ue = input("Имя:")
            if qwe == "Д":
                checke = db.exists("u>" + ue + "<a")
            else:
                checke = db.exists("u>" + ue)
            if checke == True:
                if qwe == "Д":
                    u = "u>" + ue + "<a"
                else:
                    u = "u>" + ue
                pe = input("Пароль:")
                if qwe == "Д":
                    checkp = db.get("u>" + ue + "<a")
                else:
                    checkp = db.get("u>" + ue)
                if pe != checkp:
                    print("Неправильный пароль")
                    clear()
                    continue
                else:
                    if qwe == "Д":
                        canDel = True
                    clear()
                    while True:
                        print("Добро пожаловать, %s!" % ue)
                        action = input("N - новый файл, R - читать файл,\n L - список файлов , Q - выйти,\nS - настройки, M - почта\n>")
                        if action == "N":
                            typef = input("P - для создания публичного, L - для создания приватного, ! - выход:")
                            if typef == "L":
                                    title = input("Заголовок:")
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
                                    title = input("Заголовок:")
                                    if title == "pubfiles":
                                        print("Неправильный заголовок.")
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
                            kup = input("P - публичные файлы, L - приватные файлы, ! - выход:")
                            if kup == "P":
                                door = input("Title:")
                                y = db.lexists("pubfiles", door)
                                if y == True:
                                    try:
                                        look1 = db.get(door)
                                    except:
                                        continue
                                    console.print(look1)
                                    if qwe != "Д":
                                        canDel = db.lexists(ue, y)
                                    if canDel == True:
                                        fks = input("D - удалить:")
                                        if fks == "D":
                                            fdel1 = db.lgetall("pubfiles").index(door)
                                            db.lpop("pubfiles", fdel1)
                                            db.rem(door)
                                            clear()
                                else:
                                    print("Файл не найдён")
                            elif kup == "L":
                                dur = input("Заголовок:")
                                q = db.lexists(ue, dur)
                                if q == True:
                                    try:
                                        look6 = db.get(dur)
                                    except:
                                        print("")
                                    console.print(look6)
                                    hdsa = input("D - удалить:")
                                    if hdsa == "D":
                                        db.rem(dur)
                                        db.lremvalue(ue, dur)
                                        continue
                                else:
                                    print("Файл не найдён")
                            elif kup == "!":
                                continue
                            else:
                                continue 
                        if action == "L":
                                print(Panel(str(db.lgetall("pubfiles")), title="Все публичные файлы"))
                                print(Panel(str(db.lgetall(ue)), title="Все приватные файлы"))
                        if action == "M":
                            while True:
                                print("Rmail 1.0\nN - новое письмо|R - исходящие|F - входящие|! - выход")
                                mail1 = db.get('m>' + u)
                                print(mail1)
                                dig = input('>')
                                if dig == "N":
                                    tema = input('Введите тему:')
                                    if tema == "/quit":
                                        print('Не правильный заголовок.')
                                        continue
                                    komu = input('Кому:')
                                    if not db.exists(komu):
                                        print('Нет такого почтового ящика.')
                                        continue
                                    text = input('')
                                    text = text + f'\nBy {mail1}'
                                    db.set(tema, text)
                                    db.ladd(komu, tema)
                                    db.ladd(mail1 + "<out", tema)
                                if dig == "R":
                                    print('/quit для выхода')
                                    print(Panel(str(db.lgetall(mail1 + '<out')), title="Все исходящие"))
                                    search = input('Поиск:')
                                    if search == '/quit':
                                        continue
                                    if db.lexists(mail1 + '<out', search):
                                        print(f'Темa:{search}\n{db.get(search)}')
                                    else:
                                        print("Не найдено.")
                                        continue
                                if dig == "F":
                                    print('/quit для выхода')
                                    print(Panel(str(db.lgetall(mail1)), title="Все входящие"))
                                    search = input('Поиск:')
                                    if search == '/quit':
                                        continue
                                    if db.lexists(mail1, search):
                                        print(f'Темa:{search}\n{db.get(search)}')
                                    else:
                                        print("Не найдено.")
                                        continue
                                if dig == "!":
                                    break


                        if action == "Q":
                            op = True
                            break
                        if action == "S":
                            if qwe == "Д":
                                console.print("P - поменять пароль, [bold red]D - удалить администратора[/bold red], [blue]A - Создать администратора[/blue], H - создать новость, ! - выход.")
                            else:
                                console.print("P - поменять пароль, [bold red]D - удалить пользователя[/bold red], ! - выход.")
                            jpke = input(">")
                            if jpke == "P":
                                nm = input("Пароль:")
                                gjg = db.get(u)
                                if nm != gjg:
                                    print("Неправильный пароль")
                                    continue
                                else:
                                    mn = input("Новый пароль:")
                                    db.rem(u)
                                    db.set(u, mn)
                                    continue
                            if jpke == "D":
                                if qwe == "Д":
                                    xcv = input("Имя администратора:")
                                    checkau = db.exists(xcv)
                                    if xcv == u:
                                        print("Вы ввели свое имя!")
                                    if checkau != True:
                                        print("Неправильное имя")
                                        continue
                                    xcvb = "u>" + xcv + "<a"
                                    hz = input("Вы уверены? Д/Н?")
                                    if hz == "Д":
                                        db.rem(xcvb)
                                        db.lremlist(xcv)
                                        db.lremlist(db.get('m>' + xcv))
                                        db.lremlist(db.get('m>' + xcv) + '<out')
                                        db.rem('m>' + xcv)
                                        continue
                                    
                                hz = input("Вы уверены? Д/Н?")
                                if hz == "Д":
                                    db.rem(u)
                                    db.lremlist(ue)
                                    db.lremlist(db.get('m>' + u))
                                    db.lremlist(db.get('m>' + u) + '<out')
                                    db.rem('m>' + u)
                                    op = True
                                    break
                            if qwe == "Д":
                                if jpke == "A":
                                    while True:
                                        ul = input("Выберете имя:")
                                        u = "u>" + ul + "<a"
                                        checkU = db.exists(u)
                                        if checkU == True:
                                            print("Имя занято")
                                            continue
                                        else:
                                            p = input("Выберете пароль:")
                                            mai = input("Введите название почтового ящика ({название}@rmail.sdb):")
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
                print("Неправильное имя")
                continue
    if login == "!":
        break
        
    
