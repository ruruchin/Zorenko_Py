import tkinter as tk
from tkinter import messagebox

def sign_up():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    retype_password = entry_retype_password.get()
    if username and email and password and retype_password:
        if password == retype_password:

            messagebox.showinfo("Регистрация", f"Регистрация прошла успешно!\nUsername: {username}\nEmail: {email}")
        else:
            messagebox.showerror("Ошибка", "Пароли не совпадают!")
    else:
        messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")

app = tk.Tk()
app.title("XtraForm")

app.geometry("800x700")
app.configure(bg='#000000')

frame_form = tk.Frame(app, bg='#000000')
frame_form.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

# Заголовок XtraForm
label_title = tk.Label(frame_form, text="XtraForm", font=("Helvetica", 40, "bold"), fg="#00aaff", bg='#000000')
label_title.pack(pady=10)

# Подзаголовок Bootstrap
label_subtitle = tk.Label(frame_form, text="Bootstrap 3 Xtra Form", font=("Helvetica", 24), fg="white", bg='#000000')
label_subtitle.pack(pady=3)

label_username = tk.Label(frame_form, text="Ваше имя", fg="white", bg='#000000')
label_username.pack(pady=2)
entry_username = tk.Entry(frame_form)
entry_username.pack(pady=2)

label_email = tk.Label(frame_form, text="Почта", fg="white", bg='#000000')
label_email.pack(pady=2)
entry_email = tk.Entry(frame_form)
entry_email.pack(pady=3)

label_password = tk.Label(frame_form, text="Пароль", fg="white", bg='#000000')
label_password.pack(pady=5)
entry_password = tk.Entry(frame_form, show='*')
entry_password.pack(pady=5)

label_retype_password = tk.Label(frame_form, text="Повторите пароль", fg="white", bg='#000000')
label_retype_password.pack(pady=5)
entry_retype_password = tk.Entry(frame_form, show='*')
entry_retype_password.pack(pady=5)

# Чекбокс
accept_terms = tk.Checkbutton(frame_form, text="Принимаю условия пользования", fg="white", bg='#000000')
accept_terms.pack(pady=5)

# Кнопка для регистрации
button_signup = tk.Button(frame_form, text="Зарегистрироваться", command=sign_up, bg='#007bff', fg='white')
button_signup.pack(pady=20)

label_account = tk.Label(frame_form, text="Уже есть аккаунт?", fg="white", bg='#000000')
label_account.pack(pady=1)

button_signin = tk.Button(frame_form, text="Войти", bg='#555555', fg='white')
button_signin.pack(pady=3)

app.mainloop()
