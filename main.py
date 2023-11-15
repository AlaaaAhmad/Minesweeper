from tkinter import *
from cell import Cell
import setting
import utilities

root = Tk()
root.configure(bg="Black")
root.title("Minesweeper Game")
root.geometry(str(setting.WIDTH) + 'x' + str(setting.HEIGHT))
root.resizable(False, False)

top_frame = Frame(root,
                  bg="Black",
                  height=utilities.calc_height(25),
                  width=setting.WIDTH)

top_frame.place(x=0, y=0)

left_frame = Frame(root,
                   bg="Black",
                   height=utilities.calc_height(75),
                   width=utilities.calc_width(25))

left_frame.place(x=0, y=utilities.calc_height(25))

center_frame = Frame(root,
                     bg="Black",
                     height=utilities.calc_height(75),
                     width=utilities.calc_width(75))
center_frame.place(x=utilities.calc_width(25), y=utilities.calc_height(25))

lbl = Label(top_frame,text="MineSweeper Game", font = ("", 50), fg = "White", bg = "Black")
lbl.place(x = setting.WIDTH/4, y = 0)

for x in range(setting.GRID_SIZE):
    for y in range(setting.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn(center_frame)
        c.cell_btn_obj.grid(column=y, row=x)

Cell.create_label_count(left_frame)
Cell.label_cnt_obj.place(x=0, y=0)

Cell.randomize_mines()
root.mainloop()
