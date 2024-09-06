from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4

class PicoDisplay16:
    __display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4)
    WIDTH, HEIGHT = __display.get_bounds()
    WHITE   = __display.create_pen(0xFF, 0xFF, 0xFF)
    RED     = __display.create_pen(0xFF, 0x00, 0x00)
    ORANGE  = __display.create_pen(0xFF, 0x7F, 0x00)
    YELLOW  = __display.create_pen(0xFF, 0xFF, 0x00)
    LIME    = __display.create_pen(0x00, 0xFF, 0x00)
    GREEN   = __display.create_pen(0x00, 0x7F, 0x00)
    CYAN    = __display.create_pen(0x00, 0xFF, 0xFF)
    TEAL    = __display.create_pen(0x00, 0x7F, 0x7F)
    BLUE    = __display.create_pen(0x00, 0x00, 0xFF)
    NAVY    = __display.create_pen(0x00, 0x00, 0x7F)
    PURPLE  = __display.create_pen(0x7F, 0x00, 0x7F)
    MAGENTA = __display.create_pen(0xFF, 0x00, 0xFF)
    SILVER  = __display.create_pen(0xC4, 0xC4, 0xC4)
    GREY    = __display.create_pen(0x7F, 0x7F, 0x7F)
    MAROON  = __display.create_pen(0x7F, 0x00, 0x00)
    BLACK   = __display.create_pen(0x00, 0x00, 0x00)

    def __init__(self):
        #self.display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4)
        #self.width, self.height = self.display.get_bounds()
        self.id = 5
        
        
    def clear(self, color=BLACK):
        PicoDisplay16.__display.set_pen(color)
        PicoDisplay16.__display.clear()
        PicoDisplay16.__display.update()
        


screen = PicoDisplay16()
screen.clear(PicoDisplay16.YELLOW)
#display.display.set_pen(display.WHITE)
#display.display.clear()
#display.clear()

