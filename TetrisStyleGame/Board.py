# define EMPTY as zero - when drawing cells be sure to check for EMPTY cells
EMPTY = 0
# each cell in the grid starts as empty
# and droppable
class cell:
    color    = EMPTY
    can_drop = True

    def clear(self):
        self.color    = EMPTY
        self.can_drop = True

    def __repr__(self):
        return "{}{}".format(" " if self.color == EMPTY else self.color, 
                             "↓" if self.can_drop else " ")


# default board is 20 rows and 10 columns
class board:
    def __init__(self, rows=20, columns=10):
        self.size  = (columns, rows)
        self.score = 0
        self.rows  = [[cell() for c in range(columns)] for r in range(rows)]

    def _find_full_rows(self):
        full_rows = []
        for r, row in enumerate(self.rows):
            count = 0
            for cell in row:
                if cell.color != EMPTY:
                    count += 1

            if count == len(row):
                full_rows.append(r)

        return full_rows

    def delete_full_rows(self):
        rows_to_delete = self._find_full_rows()

        if not rows_to_delete:
            return False

        count = len(rows_to_delete)
        self.score += 100 * count * count
        droppable = False

        for r in range(self.size[1]):
            for c in range(self.size[0]):
                if r in rows_to_delete:
                    droppable   = True
                    self.score += self.rows[r][c].color * count
                    self.rows[r][c].clear()
                elif droppable:
                    self.rows[r][c].can_drop = droppable

        self._print("Rows deleted {}".format(len(rows_to_delete)), DEBUG)
        return True

    def drop(self):
        dropped = 0
        for r in range(self.size[1]):
            for c in range(self.size[0]):
                current = self.rows[r][c]
                if r == 0:
                    current.can_drop = False
                else:
                    below = self.rows[r - 1][c]
                    if (current.can_drop and current.color != EMPTY
                                         and below.color   == EMPTY):
                        below.color = current.color
                        below.can_drop = True
                        current.clear()
                        dropped += 1
                    else:
                        current.can_drop = False
        if dropped > 0:
            self._print("Dropped", DEBUG)
        return dropped > 0

    def _print(self, message, is_debug):
        if is_debug:
            print(message)
            print("size   :", self.size)
            print("rows")
            for i in reversed(range(self.size[1])):
                print("{:>6} :".format(i), self.rows[i])
            print("score  :", self.score)


#'''
####################### TESTING ############################
    def _load_random(self):
        for r in range(self.size[1]):
            for c in range(self.size[0]):
                self.rows[r][c].color = random.randint(0, 6)
                self.rows[r][c].can_drop = False

import random

DEBUG = True


b = board(rows=10)
b._print('Empty Board', DEBUG)
b._load_random()
b._print('Load Random', DEBUG)
done = False
while not done:
    done = not b.drop() and not b.delete_full_rows()
    
    
b.drop()    
############################################################'''
