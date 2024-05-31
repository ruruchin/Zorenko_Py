import tkinter as tk
from tkinter import messagebox

# Словарь для перевода
slovar = {'cat': 'кошка',
     'dog': 'собака',
     'bird': 'птица',
     'mouse': 'мышь',
     'abandon': 'оставить',
     'abadate': 'забросить',
     'pet': 'питомец',
     'turtel': 'черепашка',
     'pinguin': 'пингвин',
     'punpun': 'пунпун'}


root = tk.Tk()
root.title("Англо-Русский Перевод из словаря")

root.geometry("820x220")
root.configure(bg='#000000')
label_title = tk.Label(text="Введите слово для его перевода", font=("Helvetica", 20, "bold"), fg="#00aaff", bg='#000000')
label_title.pack(pady=10)
entry = tk.Entry(root, width=30, font=("Helvetica", 20, "bold"))
entry.pack(pady=20)

entry.pack()

def translate():
    word = entry.get().lower()
    if word in slovar:
        result = slovar[word]
        messagebox.showinfo("Перевод", f"{word} - {result}")
    else:
        messagebox.showerror("Ошибка", "Слово не найдено в словаре")

button = tk.Button(root, text="Перевести", command=translate)
button.pack()


root.mainloop()
