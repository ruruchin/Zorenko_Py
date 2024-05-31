import sqlite3 as sq
from data_users import info_users

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    sex INTEGER NOT NULL DEFAULT 1, 
    old INTEGER, 
    score INTEGER
    )""")

with sq.connect('saper.db') as cur:
    con = cur.cursor()
    con.execute("INSERT INTO users VALUES (1, 'Алексей',1,22,9000)")


with sq.connect('saper.db') as cur:
    con = cur.cursor()
    con.executemany("INSERT INTO users VALUES (?,?,?,?,?)", info_users)


with sq.connect('saper.db') as cur:
    con = cur.cursor()
    con.execute("SELECT * FROM users WHERE score > 1000 ORDER BY score DESC")
    result = con.fetchall()
    print(f"{result}\n")


with sq.connect('saper.db') as cur:
    con = cur.cursor()
    con.execute("SELECT name, old, score FROM users")
    v = con.fetchall()
    print(f"СМОТРИМ КОНКРЕТНУЮ ИНФОРМАЦИЮ\n{v}\n")


with sq.connect('saper.db') as cur:
    con = cur.cursor()
    con.execute("SELECT * FROM users WHERE score < 5000")
    b = con.fetchall()
    print(f"ВЫБОРКА ПО СКОРАМ КОТОРЫЕ МЕНЬШЕ 5К\n{b}\n")


with sq.connect('saper.db') as cur:
    con = cur.cursor()
    con.execute("SELECT * FROM users WHERE score < 4000 AND sex = 1")
    sex = con.fetchall()
    print(f"ТУТ СОРТИРОВОЧКА ПО ПОЛУ И СКОРУ \n{sex}\n")


with sq.connect('saper.db') as cur:
    con = cur.cursor()
    con.execute("SELECT * FROM users WHERE name = 'Мария' ORDER BY old DESC")
    mari = con.fetchall()
    print(f"Выборка по имени и в последствии сортировка крутая по возрасту(тут по возрастанию(по умолчанию))\n{mari}\n")


with sq.connect('saper.db')as cur:
    con = cur.cursor()
    con.execute("SELECT * FROM users WHERE score > 1500 AND old > 17 ORDER BY score DESC")
    score = con.fetchall()
    print(f"Выборка по скорам и годикам жизни с последубщей их сортировкой\n{score}\n")


with sq.connect('saper.db') as cur:
    con = cur.cursor()
    con.execute("SELECT * FROM users WHERE old > 20 ORDER BY score DESC")
    one = con.fetchone()
    print(f"Берем первого нашего пользователя который был отсортирован по возрастанию его годиков жизни\n{one}\n")


with sq.connect('saper.db') as cur:
    con = cur.cursor()
    con.execute("SELECT * FROM users WHERE name = 'Мария' ORDER BY old")
    many_mari2 = con.fetchall()
    con.execute("SELECT * FROM users WHERE name = 'Мария' ORDER BY old")
    many_mari = con.fetchmany(2)
    print(f" Выборка двух другим видом фетча(Маши)\n{many_mari}\n(Это было бы при полном фетч запросе: \n{many_mari2})\n")


with sq.connect('saper.db') as cur:
    con = cur.cursor()
    con.execute("UPDATE users SET score=score+1000 WHERE name LIKE 'М%'")
    up = con.fetchall()
    print(f"С обновлением по продолжению любому(символ %)\nДля этого специально добавил еще одного юзера без Марин чтобы точнее это показать\n{up}\n")


with sq.connect('saper.db')as cur:
    con= cur.cursor()
    con.execute("DELETE FROM users WHERE user_id = 7")
    users = con.fetchall()
    print(f"Удалил здесь седьмое место\n{users}\n")







