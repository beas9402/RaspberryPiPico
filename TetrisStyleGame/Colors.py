from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P8

class canvas:
    def __init__(self):
        self._canvas = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P8)
        self.width, self.height = self._canvas.get_bounds()
        
        self.WHITE   = self._canvas.create_pen(255, 255, 255)
        self.RED     = self._canvas.create_pen(255,   0,   0)
        self.GREEN   = self._canvas.create_pen(  0, 255,   0)
        self.BLUE    = self._canvas.create_pen(  0,   0, 255)
        self.CYAN    = self._canvas.create_pen(  0, 255, 255)
        self.MAGENTA = self._canvas.create_pen(255,   0, 255)
        self.YELLOW  = self._canvas.create_pen(255, 255,   0)
        self.BLACK   = self._canvas.create_pen(  0,   0,   0)
        self.EMPTY   = self.WHITE

