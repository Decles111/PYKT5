from tkinter import Tk, Label
from datetime import datetime

root = Tk()
root.title("Что мне делать, как мне жить?")
root.geometry("800x500")
root.configure(bg="black")

Label(root, text="Мои текущие задачи", fg="yellow", bg="black", font=("IMPACT", 34, "underline")).pack(pady=20)

today = datetime.now().date()



with open("tasks.txt", "r", encoding="utf-8") as file:
    tasks = file.readlines()



for line in tasks:
    plans, ds = line.strip().split(";")

    td = datetime.strptime(ds, "%Y-%m-%d").date()

    kogda = (td - today).days

    if kogda < 0:
        text = f"Прошло {-kogda} дней от {plans}"
        color = "red"

    elif kogda == 0:
        text = f"Прямо сейчас происходит {plans}"
        color = "yellow"

    else:
        text = f"Осталось {kogda} дней до {plans}"
        color = "white"

    Label(root, text=text, fg=color, bg="black", anchor="w", font=("Arial", 14)).pack(fill="x", padx=150)

root.mainloop()