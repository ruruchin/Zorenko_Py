"""

/*телемастерская ->
/*telemaster

"""
#Сделал для того чтобы в терминале глазкам было смотреть приятнее
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

import sqlite3
from mark import mark_list
with sqlite3.Connection("database.db")as cur:
    con = cur.cursor()
    con.execute("DROP TABLE IF EXISTS users")
    con.execute("""CREATE TABLE IF NOT EXISTS users(
    prod_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mark TEXT NOT NULL DEFAULT 'Default',
    manufacture TEXT NOT NULL DEFAULT 'Default',
    price INTEGER,
    data DATA,
    document TEXT,
    master TEXT,
    cheque INTEGER
    )""")

"""    con.execute("INSERT INTO users VALUES(1,'JVC', 'JVC', 20000, 2000-01-01, 'Лицензия''гарантийный талон''инструкция', 'Тимофей', 11000)")

    con.execute("INSERT INTO users VALUES(2,'JVC', 'JVC', 80000, 2000-01-01, 'Лицензия''гарантийный талон''инструкция', 'Тимофей', 50000)")

    con.execute("INSERT INTO users VALUES(3,'JVC', 'JVC', 50000, 2000-01-01, 'Лицензия''гарантийный талон''инструкция', 'Тимофей', 20000)")

    con.execute("SELECT * FROM users")
    result = con.fetchall()
    print(f"МЫ ПОЛУЧАЕМ ТРИ ИНСЕРТА, ДАЛЕЕ БУДЕТ РАБОТА НЕПОСРЕДСТВЕННО С ИМПОРТИРОВАННОЙ ДАТА БАЗОЙ)\n{result}\n"+"-"*264)"""


with sqlite3.Connection('database.db') as cur:
    con = cur.cursor()
    con.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?)", mark_list)
    con.execute("SELECT * FROM users")
    data = con.fetchall()

    print(color.DARKCYAN + "-" * 264)
    print(f"{color.DARKCYAN}{color.BOLD}| Вставка моего списка на 10 штук: \n| {data}\n"+"-"*264+"\n"*2)


with sqlite3.Connection('database.db')as cur:
    con = cur.cursor()
    con.execute("SELECT master, data, mark FROM users ORDER BY data DESC")
    info_master = con.fetchall()
    print("-" * 264)
    print(f"{color.DARKCYAN}{color.BOLD}| МАСТЕРА И ИНФОРМАЦИЯ О ИХ ПРОДЕЛАННОЙ РАБОТЕ:\n| {info_master}\n"+"-"*264+"\n"*2)
    con.execute("SELECT master, data, mark FROM users ORDER BY data DESC")
    last_master = con.fetchmany(1)
    print("-" * 264)
    print(f"{color.DARKCYAN}{color.BOLD}| Последний работавший сотрудник(задействована дата)\n| {last_master}\n"+"-"*264+"\n"*2)


with sqlite3.Connection('database.db')as cur:
    con = cur.cursor()
    con.execute("SELECT * FROM users WHERE price > 40000 AND master = 'Игорь'")
    master_check_norma = con.fetchall()
    print("-" * 264)
    print(f"{color.DARKCYAN}{color.BOLD}| ТУТ МЫ СМОТРИМ КАКИЕ ИГОРЁК БРАЛ ЗАКАЗЫ, КОТОРЫЕ БЫ ХОРОШО СКЛАДЫВАЛИСЬ НА ЕГО ЗАРПЛАТЕ\n| {master_check_norma}\n"+"-"*264+"\n"*2)
    with sqlite3.connect('database.db')as cur:
        con = cur.cursor()
        con.execute("SELECT * FROM users WHERE price < 40000 AND master = 'Игорь'")
        master_check_min = con.fetchall()
        print("-"*264)
        print(f"{color.BOLD}| ТУТ МЫ СМОТРИМ КАКИЕ ИГОРЁК БРАЛ ЗАКАЗЫ, ОПЛАТА КОТОРЫХ БЫЛА НИЗКОЙ\n| {master_check_min}\n"+"-"*264+"\n"*2)


with sqlite3.Connection('database.db')as cur:
    con = cur.cursor()
    con.execute("SELECT * FROM users WHERE master = 'Игорь' AND price > 30000")
    old_name = con.fetchone()
    con.execute("UPDATE users SET master = 'Игорявый' WHERE master = 'Игорь' AND price > 30000")
    print("-"*264)
    print(f"| Имя которое было у сотрудника изначально ->\n| {old_name}\n|")
    con.execute("SELECT * FROM users WHERE master = 'Игорявый' AND price > 30000")
    new_name = con.fetchone()
    print(f"| Изменения имени ->\n| {new_name}\n"+"-"*264+"\n"*2)


with sqlite3.connect('database.db')as cur:
    con = cur.cursor()
    con.execute("SELECT mark, manufacture FROM users WHERE mark = 'Logitek'")
    UNO_CARD = con.fetchone()
    print("-" * 264)
    print(f"| Старая марка, которая была изначальной -> (1 значение - Марка, 2 значение - Производитель) \n| {UNO_CARD}\n|")
    con.execute("UPDATE users SET mark = 'LG' AND manufacture = 'LG' WHERE mark = 'Logitek'")
    con.execute("SELECT mark, manufacture FROM users WHERE mark = 'LG'")
    UNO_REVERSE = con.fetchone()
    print(f"| Изменения в марке, а так же в производителе -> (1 значение - Марка, 2 значение - Производитель) \n| {UNO_REVERSE}\n"+"-"*264+"\n"*2)


with sqlite3.connect('database.db')as cur:
    con = cur.cursor()
    con.execute("SELECT document FROM users")
    document_old = con.fetchone()
    print("-" * 264)
    print(f"| Изначальное оформление документов -> \n| {document_old}\n|")
    con.execute("UPDATE users SET document = 'Паспорт на холодильник'")
    con.execute("SELECT document FROM users")
    document_new = con.fetchone()
    print(f"| Изменённое оформление вывода документов -> \n| {document_new}\n"+"-"*264+"\n"*2)


with sqlite3.connect('database.db')as cur:
    con = cur.cursor()
    con.execute("DELETE FROM users WHERE master = 'Кирилл' AND cheque > 20000")
    con.execute("SELECT * FROM users WHERE master = 'Кирилл'")
    kirilla = con.fetchall()
    print("-"*264)
    print(f"| {color.UNDERLINE}Тут Кириллы, после удаления кириллов, у которых чек оплаты около 20000, но не больше!{color.END}{color.DARKCYAN}\n| {kirilla}\n"+"-"*264+"\n"*2)

with sqlite3.connect('database.db') as cur:
    con = cur.cursor()
    con.execute("DELETE FROM users WHERE master = 'Игорявый' OR(master = 'Игорь') AND cheque > 30000")
    con.execute("SELECT * FROM users WHERE master = 'Игорь'")
    Igor = con.fetchall()
    print("-" * 264)
    print(f"| {color.UNDERLINE}Тут Игорь, после удаления Игорей с зарплатой больше 30000{color.END}{color.DARKCYAN}\n| {Igor}\n" + "-" * 264 + "\n" * 2)