import pyautogui as guy
from images import *

tk['bg'] = '#ffffff'
tk.title('Arrow Circuits')
tk.iconphoto(False, appIcon)

img_width = emptyCell.width()
img_height = emptyCell.height()
window_width = img_width * 33
window_height = img_height * 18
#image resolution - width=58 x height=58

tk.geometry("{}x{}".format(window_width, window_height))

tk.resizable(width = False, height = False)

canvas = Canvas(tk, height = window_height, width = window_width)
canvas.pack()

#GRID
def coordinates_to_img_number(x, y):
    return (int(x / img_width), int(y / img_height))

def generate_list(n, val):
    result = []
    for i in range(0, n):
        result.append(val)
    return result

grid_size = (
    int(window_width / img_width) ,                    # width
    int((window_height - img_height * 3) / img_height) # height
)

def make_grid(width, height):
    return  [generate_list(width, emptyCell) for row in range(0, height)]

def make_default_grid():
    return make_grid(grid_size[0], grid_size[1])

grid = make_default_grid()

def reset_grid(grid):
    for y in len(grid):
        for x in len(grid[y]):
            grid[y][x] = emptyCell

def draw_image(imgNumber, image):
    canvas.create_image(imgNumber[0] * img_width, imgNumber[1] * img_height, anchor = NW, image = image)

def draw_grid(grid):
    for iy in range (0, len(grid)):
        for ix in range(0, len(grid[iy])):
            draw_image((ix, iy), grid[iy][ix])

def set_cell(grid, x, y, image):
    """Sets an image to cell and draws it"""
    try:
        grid[y][x] = image
        draw_image((x,y), image)
    except IndexError:
        return

draw_grid(grid)

#MENU

def make_image_tool(image):
    image_tool = lambda x,y: set_cell(grid, x, y, image)
    image_tool.name = image.name
    return image_tool

current_tool = make_image_tool(emptyCell)

def select_tool(tool):
    global current_tool
    current_tool = tool
    print(f"Selected tool: {tool.name}")

def make_rotator_tool():
    def rotator_tool(x, y):
        try:
            arrows = [arrowPointingUp, arrowPointingRight, arrowPointingDown, arrowPointingLeft]
            electrified_arrows = [electrifiedArrowPointingUp, electrifiedArrowPointingRight, electrifiedArrowPointingDown, electrifiedArrowPointingLeft]
            edges = [edgePointingFromDownLeft, edgePointingFromDownRight, edgePointingFromLeftDown, edgePointingFromLeftUp, edgePointingFromRightDown, edgePointingFromRightUp, edgePointingFromUpLeft, edgePointingFromUpRight]
            electrified_edges = [electrifiedEdgePointingFromDownLeft, electrifiedEdgePointingFromDownRight, electrifiedEdgePointingFromLeftDown, electrifiedEdgePointingFromLeftUp, electrifiedEdgePointingFromRightDown, electrifiedEdgePointingFromRightUp, electrifiedEdgePointingFromUpLeft, electrifiedEdgePointingFromUpRight]
            current_cell_image = grid[y][x]
            if current_cell_image in electrified_arrows:
                next_image = electrified_arrows[(electrified_arrows.index(current_cell_image) + 1) % len(arrows)]
            elif current_cell_image in arrows:
                next_image = arrows[(arrows.index(current_cell_image) + 1) % len(arrows)]
            elif current_cell_image in edges:
                next_image = edges[(edges.index(current_cell_image) + 1) % len(edges)]
            elif current_cell_image in electrified_edges:
                next_image = electrified_edges[(electrified_edges.index(current_cell_image) + 1) % len(electrified_edges)]
            else:
                print("This tool isn't compatible with that cell")
                return
            set_cell(grid, x, y, next_image)
        except (ValueError, IndexError):
            return
    rotator_tool.name = "Rotator"
    return rotator_tool 

menuButtonEraser = Button(tk, image = menuIconEraser, command = lambda: select_tool(make_image_tool(emptyCell)))
menuButtonEraser.place(x=50, y=img_height * 15.5)

menuButtonCreateGenerator = Button(tk, image = menuIconCreateGenerator, command = lambda: select_tool(make_image_tool(generator)))
menuButtonCreateGenerator.place(x=216, y=img_height * 15.5)

menuButtonRotator = Button(tk, image = menuIconRotator, command = lambda: select_tool(make_rotator_tool()))
menuButtonRotator.place(x=380, y=img_height * 15.5)

menuButtonArrow = Button(tk, image = menuIconArrow, command = lambda: select_tool(make_image_tool(arrowPointingUp)))
menuButtonArrow.place(x=544, y=img_height * 15.5)

menuButtonEdge = Button(tk, image = menuIconEdge, command = lambda: select_tool(make_image_tool(edgePointingFromLeftUp)))
menuButtonEdge.place(x=708, y=img_height * 15.5)

#LOGIC

class AffectedCell(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def __repr__(self) -> str:
        return f'{self.x}x{self.y}: {self.image.name}'

def make_affected_cell(x, y, image):
    return AffectedCell(x,y, image)

class CellAt(AffectedCell):
    def __init__(self, x, y):
        AffectedCell.__init__(self, x, y, grid[y][x])

def oneUpFrom(cell):
    if cell.y == 0:
        return None
    return CellAt(cell.x, cell.y - 1)

def oneLeftFrom(cell):
    if cell.x == 0:
        return None
    return CellAt(cell.x - 1, cell.y)

def oneRightFrom(cell):
    if cell.x == len(grid[0]) - 1:
        return None
    return CellAt(cell.x + 1, cell.y)

def oneDownFrom(cell):
    if cell.y == len(grid) - 1:
        return None
    return CellAt(cell.x, cell.y + 1)

def oneBackFrom(cell):
    if cell.image.gets == "left":
        return oneLeftFrom(cell)
    elif cell.image.gets == "up":
        return oneUpFrom(cell)
    elif cell.image.gets == "right":
        return oneRightFrom(cell)
    elif cell.image.gets == "down":
        return oneDownFrom(cell)

def oneFrontFrom(cell):
    if cell.image.brings == "right":
        return oneRightFrom(cell)
    elif cell.image.brings == "down":
        return oneDownFrom(cell)
    elif cell.image.brings == "left":
        return oneLeftFrom(cell)
    elif cell.image.brings == "up":
        return oneUpFrom(cell)

def invert_direction(direction):
    if direction == "right":
        return "left"
    elif direction == "left":
        return "right"
    elif direction == "up":
        return "down"
    elif direction == "down":
        return "up"

def electrifyArrowCell(arrowCell):
    """Returns electrified arrow image for a given arrow image or None if that wasn't an arrow"""
    electrifiedImage = {
        arrowPointingDown: electrifiedArrowPointingDown,
        arrowPointingRight: electrifiedArrowPointingRight,
        arrowPointingLeft: electrifiedArrowPointingLeft,
        arrowPointingUp: electrifiedArrowPointingUp,
        edgePointingFromDownLeft: electrifiedEdgePointingFromDownLeft,
        edgePointingFromDownRight: electrifiedEdgePointingFromDownRight,
        edgePointingFromLeftDown: electrifiedEdgePointingFromLeftDown,
        edgePointingFromLeftUp: electrifiedEdgePointingFromLeftUp,
        edgePointingFromRightDown: electrifiedEdgePointingFromRightDown,
        edgePointingFromRightUp: electrifiedEdgePointingFromRightUp,
        edgePointingFromUpLeft: electrifiedEdgePointingFromUpLeft,
        edgePointingFromUpRight: electrifiedEdgePointingFromUpRight
    }

    if not electrifiedImage.__contains__(arrowCell.image):
        return []

    return [AffectedCell(arrowCell.x, arrowCell.y, electrifiedImage[arrowCell.image])]

def deelectrifyArrowCell(electrifiedArrowCell):
    """Returns regular arrow image for a given electrified arrow image or None if that wasn't an electrified arrow"""
    arrowImage = {
        electrifiedArrowPointingDown: arrowPointingDown,
        electrifiedArrowPointingRight: arrowPointingRight,
        electrifiedArrowPointingLeft: arrowPointingLeft,
        electrifiedArrowPointingUp: arrowPointingUp,
        electrifiedEdgePointingFromDownLeft: edgePointingFromDownLeft,
        electrifiedEdgePointingFromDownRight: edgePointingFromDownRight,
        electrifiedEdgePointingFromLeftDown: edgePointingFromLeftDown,
        electrifiedEdgePointingFromLeftUp: edgePointingFromLeftUp,
        electrifiedEdgePointingFromRightDown: edgePointingFromRightDown,
        electrifiedEdgePointingFromRightUp: edgePointingFromRightUp,
        electrifiedEdgePointingFromUpLeft: edgePointingFromUpLeft,
        electrifiedEdgePointingFromUpRight: edgePointingFromUpRight 
    }

    if not arrowImage.__contains__(electrifiedArrowCell.image):
        return []

    return [AffectedCell(electrifiedArrowCell.x, electrifiedArrowCell.y, arrowImage[electrifiedArrowCell.image])]


def generator_behaviour(current_cell):
    affected_cells = []

    if oneLeftFrom(current_cell).image.gets == "right":
        affected_cells += electrifyArrowCell(oneLeftFrom(current_cell))
    if oneRightFrom(current_cell).image.gets == "left":
        affected_cells += electrifyArrowCell(oneRightFrom(current_cell))
    if oneUpFrom(current_cell).image.gets == "down":
        affected_cells += electrifyArrowCell(oneUpFrom(current_cell))
    if oneDownFrom(current_cell).image.gets == "up":
        affected_cells += electrifyArrowCell(oneDownFrom(current_cell))

    return affected_cells

def electrified_arrow_behaviour(current_cell):
    affected_cells = []

    if oneFrontFrom(current_cell).image in arrows and oneFrontFrom(current_cell).image.gets == invert_direction(current_cell.image.brings):
        affected_cells += electrifyArrowCell(oneFrontFrom(current_cell))

    if oneBackFrom(current_cell).image not in electrified_cells:
        affected_cells += deelectrifyArrowCell(current_cell)
        
    return affected_cells

def logic():
    affected_cells = []

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            cell = CellAt(x,y)
            if cell.image == generator:
                affected_cells += generator_behaviour(cell)
            if cell.image in electrified_arrows:
                affected_cells += electrified_arrow_behaviour(cell)

    for cell in affected_cells:
        set_cell(grid, cell.x, cell.y, cell.image)

def buttons_reaction(event):
    """ Handles a mouse click in the grid (per cell)"""
    if event.widget != canvas:
        return

    (x, y) = coordinates_to_img_number(event.x, event.y)
    current_tool(x, y)

def tick():
    """Main app timer handler: called up each tick and provides time concept for updates"""
    logic()
    tk.after(500, tick)

tk.bind('<Button-1>', buttons_reaction)
tk.after(500, tick)
tk.mainloop()