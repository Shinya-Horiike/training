from tkinter import *
from tkinter import ttk
import random

#メイン窓枠設定等
root = Tk()
root.title("0518.py GUI")


#文字書込み部
write_frame = ttk.Frame(root)
write_frame.grid()

write_label = ttk.Label(
    write_frame,
    text = "何かお話してください",
)
write_label.grid(row = 0, column = 0)

write = StringVar()
write_entry = ttk.Entry(
    write_frame,
    textvariable = write,
    width = 100
)
write_entry.grid(row = 0, column = 1)


#書込みアルゴリズム
def write_button_click():
    ram = random.randint(1,3)

    if ram%3 == 0:
        read_lb.insert(-1.0, write.get() + "\n>>> なるほど. \n")
        write_entry.delete(0, END)
    elif ram%3 == 1:
        read_lb.insert(-1.0, write.get() + "\n>>> すごいな. \n")
        write_entry.delete(0, END)
    else:
        read_lb.insert(-1.0, write.get() + "\n>>> 悪いのは君じゃない. \n")
        write_entry.delete(0, END)


write_button = ttk.Button(write_frame, text = "話す", command=write_button_click)
write_button.grid(row = 0, column = 2)

#文字表示部
read_frame = ttk.Frame(root)
read_frame.grid()

read_lb = Text(read_frame, width = 100,height = 20)
read_lb.grid()

read_Scrollbar = ttk.Scrollbar(
    read_frame,
    orient = VERTICAL,
    command = read_lb.yview
)
read_lb["yscrollcommand"] = read_Scrollbar.set
read_Scrollbar.grid(row = 0,column = 1, sticky=(N,S))

root.mainloop()