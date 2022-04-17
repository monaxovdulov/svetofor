"""В этом проекте мы создадим светофор,
который по нажатию клавиши пробел будет поочередно зажигать определенные светофоры."""
from tkinter import *
import webbrowser
from tkinter import messagebox


root = Tk() # Создаем окно  программы
root.title("Светофор") # заголовок окна
root.geometry("350x400") # размер окна
root.resizable(False, False) # запрет на изменение размеров окна
root.configure(bg="#2A4480") # цвет фона
canvas = Canvas(root, width=280, height=340, bg="#6C8CD5", relief=SOLID, bd=1) # создаем холст для отрисовки
canvas.pack() # помещаем холст на окно

def about():
    """Функция для отображения информации о программе"""
    messagebox.showinfo("О программе",
                        "Больше информации и веселых программ ты найдешь в питонах-батонах.")
    webbrowser.open_new(r"https://t.me/+zjD49vNNAZw5Mzli")

def reset_box():
    """Функция для сброса светофора"""
    canvas.itemconfig(circle_red, fill="black") # красный светофор выключен
    canvas.itemconfig(circle_yellow, fill="black") # желтый светофор выключен
    canvas.itemconfig(circle_green, fill="black") # зеленый светофор выключен

def red_light(event):
    """Функция для зажигания красного светофора"""
    canvas.itemconfig(circle_red, fill="red") # красный светофор включен
    canvas.itemconfig(circle_yellow, fill="black") # желтый светофор выключен
    canvas.itemconfig(circle_green, fill="black") # зеленый светофор выключен
    root.after(2000, yellow_light)  # запускаем функцию желтого светофора через 2 секунды


def yellow_light():
    """Функция для зажигания желтого светофора"""
    canvas.itemconfig(circle_red, fill="black") # красный светофор выключен
    canvas.itemconfig(circle_yellow, fill="yellow") # желтый светофор включен
    canvas.itemconfig(circle_green, fill="black") # зеленый светофор выключен
    root.after(2000, green_light) # запускаем функцию зеленого светофора через 2 секунды


def green_light():
    """Функция для зажигания зеленого светофора"""
    canvas.itemconfig(circle_red, fill="black") # красный светофор выключен
    canvas.itemconfig(circle_yellow, fill="black")  # желтый светофор выключен
    canvas.itemconfig(circle_green, fill="green")  # зеленый светофор включен
    root.after(2000, reset_box)

box1 = canvas.create_rectangle(90, 10, 210, 290, fill="#4a4948", outline="black") # создаем прямоугольник для светофора
box2 = canvas.create_rectangle(100, 20, 200, 280, fill="#636057", outline="black") # создаем прямоугольник для светофора
# box3 = canvas.create_rectangle(110, 30, 190, 270, fill="#7b7970", outline="black")
# box4 = canvas.create_rectangle(120, 40, 180, 260, fill="#948f84", outline="black")
# box5 = canvas.create_rectangle(130, 50, 170, 250, fill="#adab9f", outline="black")
# box6 = canvas.create_rectangle(140, 60, 160, 240, fill="#c6c4b8", outline="black")
# box7 = canvas.create_rectangle(150, 70, 150, 230, fill="#dcdad1", outline="black")
box3 = canvas.create_rectangle(140, 290, 160, 340, fill="#4a4948", outline="black") # создаем прямоугольник для светофора

circle_red = canvas.create_oval(120, 40, 180, 100, fill="red", outline="black") # создаем круг для красного светофора
circle_yellow = canvas.create_oval(120, 110, 180, 170, fill="yellow", outline="black") # создаем круг для желтого светофора
circle_green = canvas.create_oval(120, 180, 180, 240, fill="green", outline="black") # создаем круг для зеленого

reset_box() # запускаем функцию для сброса светофора
canvas.bind_all("<space>", red_light)

mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label='О программе', command=about, accelerator="Ctrl+A", underline=0)


root.mainloop()
