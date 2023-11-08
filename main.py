from tkinter import *
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
                     bg = "Black",
                     height=utilities.calc_height(75),
                     width=utilities.calc_width(75))
center_frame.place(x = utilities.calc_width(25), y = utilities.calc_height(25))
root.mainloop()
