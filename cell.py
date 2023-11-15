import sys
from tkinter import Button, Label
import random
import setting
import ctypes

class Cell:
    all_cells = []
    cell_count = setting.GRID_SIZE**2
    label_cnt_obj = None
    def __init__(self, x, y):
        self.is_mine = False
        self.is_open = False
        self.is_mine_cand = False
        self.cell_btn_obj = None
        self.x = x
        self.y = y

        Cell.all_cells.append(self)

    def create_btn(self, location):
        btn = Button(location,
                     width=9,
                     height=3,
                     bg="White")

        btn.bind('<Button-1>', self.on_left_clicked)
        btn.bind('<Button-3>', self.on_right_clicked)


        self.cell_btn_obj = btn

    def on_right_clicked(self, event):
        if not self.is_mine_cand:
            self.cell_btn_obj.configure(bg = "Blue")
            self.is_mine_cand = True
        else:
            self.cell_btn_obj.configure(bg = "White")
            self.is_mine_cand = False
    def on_left_clicked(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines() == 0:
                for i in self.surrounded_cells():
                    i.show_cell()
            self.show_cell()

    def show_mine(self):
        self.cell_btn_obj.configure(bg="Red")
        ctypes.windll.user32.MessageBoxW(0,"You Clicked A Mine", "Game Over", 0)
        sys.exit()



    def show_cell(self):
        if not self.is_open:
          self.cell_btn_obj.configure(text=self.surrounded_cells_mines(), bg = "Orange")
          Cell.cell_count -= 1
          if Cell.label_cnt_obj:
              Cell.label_cnt_obj.configure(text = "Cells Left: "+str(Cell.cell_count))
          if Cell.cell_count == setting.MINES_COUNT:
              for cell in Cell.all_cells:
                  cell.configure(bg = "Green")
                  ctypes.windll.user32.MessageBoxW(0, "You Finished All the cells", "Great Job!", 0)
                  sys.exit()


        self.is_open = True



    def get_cell(self, x, y):
        for cell in Cell.all_cells:
            if cell.x == x and cell.y == y:
                return cell
    def surrounded_cells(self):
        cells = [
            self.get_cell(self.x-1, self.y - 1),
            self.get_cell(self.x - 1, self.y),
            self.get_cell(self.x - 1, self.y + 1),
            self.get_cell(self.x, self.y - 1),
            self.get_cell(self.x, self.y + 1),
            self.get_cell(self.x + 1, self.y - 1),
            self.get_cell(self.x + 1, self.y + 1),
            self.get_cell(self.x + 1, self.y)

        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    def surrounded_cells_mines(self):
        cnt = 0
        for cell in self.surrounded_cells():
            if cell.is_mine:
                cnt += 1
        return cnt


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all_cells, setting.MINES_COUNT)
        for i in picked_cells:
            i.is_mine = True


    @staticmethod
    def create_label_count(location):
        label = Label(location,
                      text="Cells Left: "+str(Cell.cell_count),
                      fg = "White",
                      bg = "Black",
                      width=12,
                      height=4,
                      font=("", 30))

        Cell.label_cnt_obj = label
