import time
from Colors import *
from Board import Board
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P8

class TetrisDisplay:
    _colors = DEFINED_COLORS
    def __init__(self, display: PicoGraphics, board: Board):
        self.display = display
        self.board = board
        self.width, self.height = self.display.get_bounds()

        # figure out the best cell size for this display
        col_fit = (int)((self.width-1)/self.board.size[0])
        row_fit = (int)((self.height-1)/self.board.size[1])
        self.cell_size    = min(col_fit, row_fit)
        self.board_width  = (int)(self.cell_size*self.board.size[0])+1
        self.board_height = (int)(self.cell_size*self.board.size[1])+1
        self.board_x      = (int)((self.width-self.board_width)/2)
        self.board_y      = (int)((self.height-self.board_height)/2)
        for c in TetrisDisplay._colors:
            self.display.create_pen(c.rgb[0],c.rgb[1],c.rgb[2])

    def draw_board(self):
        print('***************** DRAW *************')
        self.display.set_pen(YELLOW.index)
        self.display.clear()
        self.display.set_pen(WHITE.index)
        self.display.rectangle(self.board_x, self.board_y, self.board_width, self.board_height)
        
        for r, row in enumerate(self.board.rows):
            for c, cell in enumerate(row):
                if cell.color != 0:
                    cell_x = (c * self.cell_size) + self.board_x
                    cell_y = (r * self.cell_size) + self.board_y
                    self.display.set_pen(BLACK.index)
                    self.display.rectangle(cell_x, cell_y,
                                           self.cell_size+1, self.cell_size+1)
                    self.display.set_pen(cell.color)
                    self.display.rectangle(cell_x+1, cell_y+1, self.cell_size-1,
                                           self.cell_size-1)
 
        self.display.update()

        
    
    def clear(self, color):
        print(color)
        self.display.set_pen(color.index)
        self.display.clear()


if __name__ == "__main__":
    x = TetrisDisplay(PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P8), Board(rows=20))
    x.board._load_random()
    x.draw_board()
    game_over = False
    while not game_over:
        done = False
        while not done:
            time.sleep(0.1)
            dropped = x.board.drop()
            x.draw_board()
            deleted = x.board.delete_full_rows()
            if deleted:
                time.sleep(0.1)
                x.draw_board()
            done = not dropped and not deleted
        
        row19 = x.board.rows[19]
        game_over = (row19[3].color + row19[4].color + row19[5].color + row19[6].color) > 0
        if not game_over:
            row19[3].color = 3
            row19[3].can_drop = True
            row19[4].color = 3
            row19[4].can_drop = True
            row19[5].color = 3
            row19[5].can_drop = True
            row19[6].color = 3
            row19[6].can_drop = True


    x.board._print("done", True)
    #while True:
    #    time.sleep(0.5)
    #    x.board.drop()
    #    x.board.delete_full_rows()
    #    x.draw_board()
    #x.draw_rect(0,0,10,10,GREEN)

    #col_fit = (int)(x.width/x.board.size[0])
    ##row_fit = (int)(x.height/x.board.size[1])
    #fit = min(col_fit, row_fit)
    #print(x.width)
    #print(col_fit)
    #print(x.height)
    #print(row_fit)
    print(x.cell_size)
