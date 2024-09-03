#include Colors.py

EMPTY = 0

class cell:
    state    = EMPTY
    can_drop = True
    def __init__(self):
        return
    def __repr__(self):
        return '{}{}'.format(' ' if self.state == EMPTY else self.state,
                                   '↓' if self.can_drop else ' ')
    def clear(self):
        self.state = EMPTY
        self.can_drop = True

class board:
    def __init__(self, x, y, rows=20, columns=10, brick=10):
        self.origin = (x, y)
        self.size   = (columns, rows)
        self.brick  = brick
        self.center = brick-2
        self.stride = brick + 1
        self.wide   = (self.stride * columns) + 1
        self.high   = (self.stride * rows)    + 1
        self.score  = 0
        self.delete = []
        #self.empty  = []
        self.rows   = [[cell() for c in range(columns)]
                                    for r in range(rows)]

        
    def clear_delete(self):
        delete_count = len(self.delete)
        self.score  += (100 * delete_count)
        top          =  self.size[0] - 1
        droppable    = False
        for r in range(self.size[1]):
            for c in range(self.size[0]):
                #print(r, c, r in self.delete)
                if r in self.delete:
                    droppable = True
                    self.score += (self.rows[r][c].state * delete_count)
                    self.rows[r][c].clear()
                elif droppable:
                    self.rows[r][c].can_drop = droppable
        self.delete = []
        
    def compact_bricks(self):
        first = 0 # self.empty.pop(0)
        
        for r in range(self.size[1]):
            for c in range(self.size[0]):
                current = self.rows[r][c]
                if r == 0:
                    current.can_drop = False
                else:
                    below = self.rows[r-1][c]
                    if current.can_drop and below.state == EMPTY:
                        below.state = current.state
                        below.can_drop = True
                        current.clear()
                    else:
                        current.can_drop == False
        #self.empty = []

    def draw(self, board, ):
        print('***************** DRAW *************')
        x, y = self.origin
        canvas.set_pen(BLACK)
        canvas.clear()
        canvas.set_pen(WHITE)
        canvas.rectangle(x, y, self.wide, self.high)

        for r, row in enumerate(self.rows):
            drawcount = 0
            for c, cell in enumerate(row):
                if cell.state != EMPTY:
                    cell_x = (c * self.stride) + x + 1
                    cell_y = ((self.size[1]-1 - r) * self.stride) + y + 1
                    canvas.set_pen(BLACK)
                    canvas.rectangle(cell_x, cell_y, self.brick, self.brick)
                    canvas.set_pen(cell.state)
                    canvas.rectangle(cell_x + 1, cell_y + 1, self.center, self.center)
                    drawcount += 1
                    
            if drawcount == len(row):
                self.delete.append(r)


        canvas.update()
        self._print()   
    def _find_full_rows(self):
        for r, row in enumerate(self.rows):
            count = 0
            for c, cell in enumerate(row):
                if cell.state != EMPTY:
                    count += 1
                    
            if count == len(row):
                self.delete.append(r)
  
 
    def _print(self, all=False):
        if all:
            print('origin :', self.origin)
            print('size   :', self.size)
            print('brick  :', self.brick)
            print('center :', self.center)
            print('stride :', self.stride)
            print('wide   :', self.wide )
            print('high   :', self.high)
        print('rows')
        for i in reversed(range(self.size[1])):
            print('{:>6} :'.format(i), self.rows[i])
        
        print('score  :', self.score )
        print('delete :', self.delete )

    def _load_random(self):
        for r in range(self.size[1]):
            for c in range(self.size[0]):
                self.rows[r][c].state = random.randint(0, 6)
                self.rows[r][c].can_drop = False
 
 
 
####################### TESTING ############################
import time
import random


b = board(x=11, y=0, rows=10)
b._print()
b._load_random()
b._print()
b._find_full_rows()
b._print()