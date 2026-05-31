from tkinter import Tk, Label
from datetime import datetime


def read_file():
    with open("tasks.txt", "r", encoding="utf-8") as file:
        return file.readlines()


def color(days):
    if days < 0:
        return "red"
    if days == 0:
        return "yellow"
    return "white"


def make_list(tasks):
    old = []
    now = []
    fu = []
    k = 0

    td = datetime.now().date()

    for line in tasks:
        k += 1

        plan, date = line.strip().split(";")
        date = datetime.strptime(date, "%Y-%m-%d").date()

        days = (date - td).days

        if days < 0:
            old.append([f"Прошло {-days} дней от {plan}", days])
        elif days == 0:
            now.append([f"Прямо сейчас происходит {plan}", days])
        else:
            fu.append([f"Осталось {days} дней до {plan}", days])

    old = sorted(old, key=lambda x: x[1])
    fu = sorted(fu, key=lambda x: x[1])

    return old + now + fu, k


root = Tk()
root.title("Что мне делать, как мне жить?")
root.configure(bg="black")

Label(root,text="Мои текущие задачи",fg="yellow",bg="black",font=("IMPACT", 34, "underline")).pack(pady=20)

tasks = read_file()

data, k = make_list(tasks)

root.geometry(f"1000x{200 + k * 25}")

for text, days in data:
    Label(root,text=text,fg=color(days),bg="black",anchor="w",font=("Arial", 14)).pack(fill="x", padx=30)

root.mainloop()
