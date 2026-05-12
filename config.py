from models import Size

SCREEN_SIZE = Size(800, 800)

CELL_SIZE = 20
GRID_WIDTH: int = SCREEN_SIZE.width // CELL_SIZE
GRID_HEIGHT: int = SCREEN_SIZE.height // CELL_SIZE
