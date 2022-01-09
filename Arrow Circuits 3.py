from tkinter import *
import pyautogui as guy

tk = Tk()
tk['bg'] = '#ffffff'
tk.title('Arrow Circuits')
tk.iconphoto(False, PhotoImage(file="resources/arrow_circuits_icon.ico"))

emptyCell = PhotoImage(name="Eraser", file="resources/empty_cell.png")
generator = PhotoImage(name="Create generator", file="resources/generator.png")
arrowPointingUp = PhotoImage(name="Arrow", file="resources/arrow_pUP.png")
arrowPointingDown = PhotoImage(name="a_d", file="resources/arrow_pDOWN.png")
arrowPointingLeft = PhotoImage(name="a_l", file="resources/arrow_pLEFT.png")
arrowPointingRight = PhotoImage(name="a_r", file="resources/arrow_pRIGHT.png")
electrifiedArrowPointingUp = PhotoImage(name = "ea_u", file="resources/electrified_arrow_pUP.png")
electrifiedArrowPointingDown = PhotoImage(name = "ea_d", file="resources/electrified_arrow_pDOWN.png")
electrifiedArrowPointingLeft = PhotoImage(name = "ea_l", file="resources/electrified_arrow_pLEFT.png")
electrifiedArrowPointingRight = PhotoImage(name = "ea_r", file="resources/electrified_arrow_pRIGHT.png")

menuIconArrow = PhotoImage(file="resources/arrow_menu_icon.png")
menuIconCreateGenerator = PhotoImage(file="resources/create_generator_menu_icon.png")
menuIconEraser = PhotoImage(file="resources/eraser_menu_icon.png")
menuIconRotator = PhotoImage(file="resources/rotator_menu_icon.png")

img_width = emptyCell.width()
img_height = emptyCell.height()
window_width = img_width * 33
window_height = img_height * 18
#image resolution - width=57 x height=57

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
            current_cell_image = grid[y][x]
            if current_cell_image in electrified_arrows:
                next_image = electrified_arrows[(electrified_arrows.index(current_cell_image) + 1) % len(arrows)]
            elif current_cell_image in arrows:
                next_image = arrows[(arrows.index(current_cell_image) + 1) % len(arrows)]
            else:
                print("This tool isn't compatible with that cell")
                return
            set_cell(grid, x, y, next_image)
        except (ValueError, IndexError):
            return
    rotator_tool.name = "Rotator"
    return rotator_tool 

menuButtonEraser = Button(tk, image = menuIconEraser, command = lambda: select_tool(make_image_tool(emptyCell)))
menuButtonEraser.place(x=50, y= img_height * 15.5)

menuButtonCreateGenerator = Button(tk, image = menuIconCreateGenerator, command = lambda: select_tool(make_image_tool(generator)))
menuButtonCreateGenerator.place(x=214, y= img_height * 15.5)

menuButtonRotator = Button(tk, image = menuIconRotator, command = lambda: select_tool(make_rotator_tool()))
menuButtonRotator.place(x=378, y= img_height * 15.5)

menuButtonArrow = Button(tk, image = menuIconArrow, command = lambda: select_tool(make_image_tool(arrowPointingUp)))
menuButtonArrow.place(x=542, y= img_height * 15.5)

#LOGIC


arrows = [arrowPointingUp,
          arrowPointingRight,
          arrowPointingDown,
          arrowPointingLeft]

electrified_arrows = [electrifiedArrowPointingUp,
                      electrifiedArrowPointingRight,
                      electrifiedArrowPointingLeft,
                      electrifiedArrowPointingDown]

electrified_cells = electrified_arrows + [generator]

class AffectedCell(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def __repr__(self) -> str:
        return f'{self.x}x{self.y}: {self.image.name}'

def make_affected_cell(x, y, image):
    return AffectedCell(x,y, image)

class CellAt(AffectedCell): # I rename AffectedCell to CellAt for readability
    def __init__(self, x, y):
        AffectedCell.__init__(self, x, y, grid[y][x])

def oneUpFrom(fromCell):
    if fromCell.y == 0:
        return None
    return CellAt(fromCell.x, fromCell.y - 1)

def oneLeftFrom(fromCell):
    if fromCell.x == 0:
        return None
    return CellAt(fromCell.x - 1, fromCell.y)

def oneRightFrom(fromCell):
    if fromCell.x == len(grid[0]) - 1:
        return None
    return CellAt(fromCell.x + 1, fromCell.y)

def oneDownFrom(fromCell):
    if fromCell.y == len(grid) - 1:
        return None
    return CellAt(fromCell.x, fromCell.y + 1)

def oneBackFrom(fromCell):
    if fromCell.image == arrowPointingRight or fromCell.image == electrifiedArrowPointingRight:
        return oneLeftFrom(fromCell)
    elif fromCell.image == arrowPointingDown or fromCell.image == electrifiedArrowPointingDown:
        return oneUpFrom(fromCell)
    elif fromCell.image == arrowPointingLeft or fromCell.image == electrifiedArrowPointingLeft:
        return oneRightFrom(fromCell)
    elif fromCell.image == arrowPointingUp or fromCell.image == electrifiedArrowPointingUp:
        return oneDownFrom(fromCell)

def electrifyArrowCell(arrowCell):
    """Returns electrified arrow image for a given arrow image or None if that wasn't an arrow"""
    electrifiedImage = {
        arrowPointingDown: electrifiedArrowPointingDown,
        arrowPointingRight: electrifiedArrowPointingRight,
        arrowPointingLeft: electrifiedArrowPointingLeft,
        arrowPointingUp: electrifiedArrowPointingUp
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
        electrifiedArrowPointingUp: arrowPointingUp
    }

    if not arrowImage.__contains__(electrifiedArrowCell.image):
        return []

    return [AffectedCell(electrifiedArrowCell.x, electrifiedArrowCell.y, arrowImage[electrifiedArrowCell.image])]


def arrow_behaviour(current_cell):
    if oneBackFrom(current_cell).image in electrified_cells:
        return [electrifyArrowCell(current_cell)]

    return []

def electrified_arrow_behaviour(current_cell):
    if oneBackFrom(current_cell).image not in electrified_cells:
        return [deelectrifyArrowCell(current_cell)]
        
    return []

def update_grid():
    affected_cells = []

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            cell = CellAt(x,y)
            if cell.image in arrows :
                affected_cells += arrow_behaviour(cell)
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
    update_grid()
    tk.after(500, tick)

tk.bind('<Button-1>', buttons_reaction)
tk.after(500, tick)
tk.mainloop()