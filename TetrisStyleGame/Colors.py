class Color:
    _auto_index = 0
    KNOWN = []
    
    def __init__(self, name: str, rgb: tuple[int, int, int]=(), index: int=None):
        self.name = name
        self.rgb  = rgb
        
        # unless we are reusing an index add it to out defined colors  
        if index is None:
            self.index = len(Color.DEFINED_COLORS)
            Color.KNOWN.append(self)
        else:
            self.index = index

    def __repr__(self):
        return "{}(index:{} rgb:{})".format(self.name,
                                            self.index,
                                            str(self.rgb).replace('(','').replace(')','').replace(' ',''))



# CONSTANTS for the basic 8
WHITE   = Color('WHITE',   (255, 255, 255))
RED     = Color('RED',     (255,   0,   0))
GREEN   = Color('GREEN',   (  0, 255,   0))
BLUE    = Color('BLUE',    (  0,   0, 255))
CYAN    = Color('CYAN',    (  0, 255, 255))
MAGENTA = Color('MAGENTA', (255,   0, 255))
YELLOW  = Color('YELLOW',  (255, 255,   0))
BLACK   = Color('BLACK',   (  0,   0,   0))
#CONSTANT for EMPTY
EMPTY   = Color('EMPTY',   index=WHITE.index )
