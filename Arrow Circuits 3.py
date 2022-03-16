import pyautogui as guy
from images import *

tk['bg'] = '#ffffff'
tk.title('Arrow Circuits')
tk.iconphoto(False, appIcon)

IMG_WIDTH = emptyCell.width()
IMG_HEIGHT = emptyCell.height()
WINDOW_WIDTH = IMG_WIDTH * 33
WINDOW_HEIGHT = IMG_HEIGHT * 18
#image resolution - width=58 x height=58

tk.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))

tk.resizable(width = False, height = False)

CANVAS = Canvas(tk, height = WINDOW_HEIGHT, width = WINDOW_WIDTH)
CANVAS.pack()

#GRID

def lower_first_letter(string):
   if len(string) == 0:
      return string
   else:
      return string[0].lower() + string[1:]

def coordinates_to_img_number(x, y):
    return (int(x / IMG_WIDTH), int(y / IMG_HEIGHT))

def generate_list(n, val):
    result = []
    for i in range(0, n):
        result.append(val)
    return result

grid_size = (
    int(WINDOW_WIDTH / IMG_WIDTH) ,                    # width
    int((WINDOW_HEIGHT - IMG_HEIGHT * 3) / IMG_HEIGHT) # height
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
    CANVAS.create_image(imgNumber[0] * IMG_WIDTH, imgNumber[1] * IMG_HEIGHT, anchor = NW, image = image)

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
    return image_tool

current_tool = make_image_tool(emptyCell)

def select_tool(tool):
    global current_tool
    current_tool = tool

def make_configurator_tool():
    def configurator_tool(x, y):
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
            elif current_cell_image in empty_conveyors:
                next_image = empty_conveyors[(empty_conveyors.index(current_cell_image) + 1) % len(empty_conveyors)]
            else:
                print("Configurator isn't compatible with that cell")
                return
            set_cell(grid, x, y, next_image)
        except (ValueError, IndexError):
            return
    return configurator_tool 

menuButtonEraser = Button(tk, image = menuIconEraser, command = lambda: select_tool(make_image_tool(emptyCell)))
menuButtonEraser.place(x=50, y=IMG_HEIGHT * 15.5)

menuButtonGenerator = Button(tk, image = menuIconGenerator, command = lambda: select_tool(make_image_tool(generator)))
menuButtonGenerator.place(x=216, y=IMG_HEIGHT * 15.5)

menuButtonconfigurator = Button(tk, image = menuIconConfigurator, command = lambda: select_tool(make_configurator_tool()))
menuButtonconfigurator.place(x=380, y=IMG_HEIGHT * 15.5)

menuButtonArrow = Button(tk, image = menuIconArrow, command = lambda: select_tool(make_image_tool(arrowPointingUp)))
menuButtonArrow.place(x=544, y=IMG_HEIGHT * 15.5)

menuButtonEdge = Button(tk, image = menuIconEdge, command = lambda: select_tool(make_image_tool(edgePointingFromLeftUp)))
menuButtonEdge.place(x=708, y=IMG_HEIGHT * 15.5)

menuButtonInverter = Button(tk, image = menuIconInverter, command = lambda: select_tool(make_image_tool(inverter)))
menuButtonInverter.place(x=872, y=IMG_HEIGHT * 15.5)

menuButtonConveyor = Button(tk, image = menuIconConveyor, command = lambda: select_tool(make_image_tool(conveyorPointingUp)))
menuButtonConveyor.place(x=1036, y=IMG_HEIGHT * 15.5)

#LOGIC

arrows = [arrowPointingUp,
          arrowPointingRight,
          arrowPointingDown,
          arrowPointingLeft,
          edgePointingFromDownLeft,
          edgePointingFromDownRight,
          edgePointingFromLeftDown,
          edgePointingFromLeftUp,
          edgePointingFromRightDown,
          edgePointingFromRightUp,
          edgePointingFromUpLeft,
          edgePointingFromUpRight]

electrified_arrows = [electrifiedArrowPointingUp,
                      electrifiedArrowPointingRight,
                      electrifiedArrowPointingLeft,
                      electrifiedArrowPointingDown,
                      electrifiedEdgePointingFromDownLeft,
                      electrifiedEdgePointingFromDownRight,
                      electrifiedEdgePointingFromLeftDown,
                      electrifiedEdgePointingFromLeftUp,
                      electrifiedEdgePointingFromRightDown,
                      electrifiedEdgePointingFromRightUp,
                      electrifiedEdgePointingFromUpLeft,
                      electrifiedEdgePointingFromUpRight]

electrified_cells = [electrifiedArrowPointingUp,
                     electrifiedArrowPointingRight,
                     electrifiedArrowPointingLeft,
                     electrifiedArrowPointingDown,
                     electrifiedEdgePointingFromDownLeft,
                     electrifiedEdgePointingFromDownRight,
                     electrifiedEdgePointingFromLeftDown,
                     electrifiedEdgePointingFromLeftUp,
                     electrifiedEdgePointingFromRightDown,
                     electrifiedEdgePointingFromRightUp,
                     electrifiedEdgePointingFromUpLeft,
                     electrifiedEdgePointingFromUpRight,
                     electrifiedInverter,
                     generator]

empty_conveyors = [conveyorPointingUp, 
                   conveyorPointingRight, 
                   conveyorPointingDown, 
                   conveyorPointingLeft]

conveyors_containing_cells = [conveyorPointingUpContainingGenerator,
                              conveyorPointingUpContainingArrowPointingUp,
                              conveyorPointingUpContainingArrowPointingDown,
                              conveyorPointingUpContainingArrowPointingLeft,
                              conveyorPointingUpContainingArrowPointingRight,
                              conveyorPointingUpContainingElectrifiedArrowPointingUp,
                              conveyorPointingUpContainingElectrifiedArrowPointingDown,
                              conveyorPointingUpContainingElectrifiedArrowPointingLeft,
                              conveyorPointingUpContainingElectrifiedArrowPointingRight,
                              conveyorPointingUpContainingEdgePointingFromDownLeft,
                              conveyorPointingUpContainingEdgePointingFromDownRight,
                              conveyorPointingUpContainingEdgePointingFromLeftDown,
                              conveyorPointingUpContainingEdgePointingFromLeftUp,
                              conveyorPointingUpContainingEdgePointingFromRightDown,
                              conveyorPointingUpContainingEdgePointingFromRightUp,
                              conveyorPointingUpContainingEdgePointingFromUpLeft,
                              conveyorPointingUpContainingEdgePointingFromUpRight,
                              conveyorPointingUpContainingElectrifiedEdgePointingFromDownLeft,
                              conveyorPointingUpContainingElectrifiedEdgePointingFromDownRight,
                              conveyorPointingUpContainingElectrifiedEdgePointingFromLeftDown,
                              conveyorPointingUpContainingElectrifiedEdgePointingFromLeftUp,
                              conveyorPointingUpContainingElectrifiedEdgePointingFromRightDown,
                              conveyorPointingUpContainingElectrifiedEdgePointingFromRightUp,
                              conveyorPointingUpContainingElectrifiedEdgePointingFromUpLeft,
                              conveyorPointingUpContainingElectrifiedEdgePointingFromUpRight,
                              conveyorPointingUpContainingInverter,
                              conveyorPointingUpContainingElectrifiedInverter,
                              conveyorPointingUpContainingConveyorPointingUp,
                              conveyorPointingUpContainingConveyorPointingLeft,
                              conveyorPointingUpContainingConveyorPointingDown,
                              conveyorPointingUpContainingConveyorPointingRight,
                              conveyorPointingLeftContainingGenerator,
                              conveyorPointingLeftContainingArrowPointingUp,
                              conveyorPointingLeftContainingArrowPointingDown,
                              conveyorPointingLeftContainingArrowPointingLeft,
                              conveyorPointingLeftContainingArrowPointingRight,
                              conveyorPointingLeftContainingElectrifiedArrowPointingUp,
                              conveyorPointingLeftContainingElectrifiedArrowPointingDown,
                              conveyorPointingLeftContainingElectrifiedArrowPointingLeft,
                              conveyorPointingLeftContainingElectrifiedArrowPointingRight,
                              conveyorPointingLeftContainingEdgePointingFromDownLeft,
                              conveyorPointingLeftContainingEdgePointingFromDownRight,
                              conveyorPointingLeftContainingEdgePointingFromLeftDown,
                              conveyorPointingLeftContainingEdgePointingFromLeftUp,
                              conveyorPointingLeftContainingEdgePointingFromRightDown,
                              conveyorPointingLeftContainingEdgePointingFromRightUp,
                              conveyorPointingLeftContainingEdgePointingFromUpLeft,
                              conveyorPointingLeftContainingEdgePointingFromUpRight,
                              conveyorPointingLeftContainingElectrifiedEdgePointingFromDownLeft,
                              conveyorPointingLeftContainingElectrifiedEdgePointingFromDownRight,
                              conveyorPointingLeftContainingElectrifiedEdgePointingFromLeftDown,
                              conveyorPointingLeftContainingElectrifiedEdgePointingFromLeftUp,
                              conveyorPointingLeftContainingElectrifiedEdgePointingFromRightDown,
                              conveyorPointingLeftContainingElectrifiedEdgePointingFromRightUp,
                              conveyorPointingLeftContainingElectrifiedEdgePointingFromUpLeft,
                              conveyorPointingLeftContainingElectrifiedEdgePointingFromUpRight,
                              conveyorPointingLeftContainingInverter,
                              conveyorPointingLeftContainingElectrifiedInverter,
                              conveyorPointingLeftContainingConveyorPointingUp,
                              conveyorPointingLeftContainingConveyorPointingLeft,
                              conveyorPointingLeftContainingConveyorPointingDown,
                              conveyorPointingLeftContainingConveyorPointingRight,
                              conveyorPointingRightContainingGenerator,
                              conveyorPointingRightContainingArrowPointingUp,
                              conveyorPointingRightContainingArrowPointingDown,
                              conveyorPointingRightContainingArrowPointingLeft,
                              conveyorPointingRightContainingArrowPointingRight,
                              conveyorPointingRightContainingElectrifiedArrowPointingUp,
                              conveyorPointingRightContainingElectrifiedArrowPointingLeft,
                              conveyorPointingRightContainingElectrifiedArrowPointingRight,
                              conveyorPointingRightContainingEdgePointingFromDownLeft,
                              conveyorPointingRightContainingEdgePointingFromDownRight,
                              conveyorPointingRightContainingEdgePointingFromLeftDown,
                              conveyorPointingRightContainingEdgePointingFromLeftUp,
                              conveyorPointingRightContainingEdgePointingFromRightDown,
                              conveyorPointingRightContainingEdgePointingFromRightUp,
                              conveyorPointingRightContainingEdgePointingFromUpLeft,
                              conveyorPointingRightContainingEdgePointingFromUpRight,
                              conveyorPointingRightContainingElectrifiedEdgePointingFromDownLeft,
                              conveyorPointingRightContainingElectrifiedEdgePointingFromDownRight,
                              conveyorPointingRightContainingElectrifiedEdgePointingFromLeftDown,
                              conveyorPointingRightContainingElectrifiedEdgePointingFromLeftUp,
                              conveyorPointingRightContainingElectrifiedEdgePointingFromRightDown,
                              conveyorPointingRightContainingElectrifiedEdgePointingFromRightUp,
                              conveyorPointingRightContainingElectrifiedEdgePointingFromUpLeft,
                              conveyorPointingRightContainingElectrifiedEdgePointingFromUpRight,
                              conveyorPointingRightContainingInverter,
                              conveyorPointingRightContainingElectrifiedInverter,
                              conveyorPointingRightContainingConveyorPointingUp,
                              conveyorPointingRightContainingConveyorPointingLeft,
                              conveyorPointingRightContainingConveyorPointingDown,
                              conveyorPointingRightContainingConveyorPointingRight,
                              conveyorPointingDownContainingGenerator,
                              conveyorPointingDownContainingArrowPointingUp,
                              conveyorPointingDownContainingArrowPointingDown,
                              conveyorPointingDownContainingArrowPointingLeft,
                              conveyorPointingDownContainingArrowPointingRight,
                              conveyorPointingDownContainingElectrifiedArrowPointingUp,
                              conveyorPointingDownContainingElectrifiedArrowPointingDown,
                              conveyorPointingDownContainingElectrifiedArrowPointingLeft,
                              conveyorPointingDownContainingElectrifiedArrowPointingRight,
                              conveyorPointingDownContainingEdgePointingFromDownLeft,
                              conveyorPointingDownContainingEdgePointingFromDownRight,
                              conveyorPointingDownContainingEdgePointingFromLeftDown,
                              conveyorPointingDownContainingEdgePointingFromLeftUp,
                              conveyorPointingDownContainingEdgePointingFromRightDown,
                              conveyorPointingDownContainingEdgePointingFromRightUp,
                              conveyorPointingDownContainingEdgePointingFromUpLeft,
                              conveyorPointingDownContainingElectrifiedEdgePointingFromDownLeft,
                              conveyorPointingDownContainingElectrifiedEdgePointingFromDownRight,
                              conveyorPointingDownContainingElectrifiedEdgePointingFromLeftDown,
                              conveyorPointingDownContainingElectrifiedEdgePointingFromLeftUp,
                              conveyorPointingDownContainingElectrifiedEdgePointingFromRightDown,
                              conveyorPointingDownContainingElectrifiedEdgePointingFromRightUp,
                              conveyorPointingDownContainingElectrifiedEdgePointingFromUpLeft,
                              conveyorPointingDownContainingElectrifiedEdgePointingFromUpRight,
                              conveyorPointingDownContainingInverter,
                              conveyorPointingDownContainingElectrifiedInverter,
                              conveyorPointingDownContainingConveyorPointingUp,
                              conveyorPointingDownContainingConveyorPointingLeft,
                              conveyorPointingDownContainingConveyorPointingDown,
                              conveyorPointingDownContainingConveyorPointingRight]

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

def one_up_from(cell):
    if cell.y == 0:
        return None
    if CellAt(cell.x, cell.y - 1).image.deleted == True:
        return None
    return CellAt(cell.x, cell.y - 1)

def one_left_from(cell):
    if cell.x == 0:
        return None
    if CellAt(cell.x - 1, cell.y).image.deleted == True:
        return None
    return CellAt(cell.x - 1, cell.y)

def one_right_from(cell):
    if cell.x == len(grid[0]) - 1:
        return None
    if CellAt(cell.x + 1, cell.y).image.deleted == True:
        return None
    return CellAt(cell.x + 1, cell.y)

def one_down_from(cell):
    if cell.y == len(grid) - 1:
        return None
    if CellAt(cell.x, cell.y + 1).image.deleted == True:
        return None
    return CellAt(cell.x, cell.y + 1)

def one_back_from(cell):
    if cell.image.gets == "left":
        return one_left_from(cell)
    elif cell.image.gets == "up":
        return one_up_from(cell)
    elif cell.image.gets == "right":
        return one_right_from(cell)
    elif cell.image.gets == "down":
        return one_down_from(cell)

def one_front_from(cell):
    if cell.image.gives == "right":
        return one_right_from(cell)
    elif cell.image.gives == "down":
        return one_down_from(cell)
    elif cell.image.gives == "left":
        return one_left_from(cell)
    elif cell.image.gives == "up":
        return one_up_from(cell)

def invert_direction(direction):
    if direction == "right":
        return "left"
    elif direction == "left":
        return "right"
    elif direction == "up":
        return "down"
    elif direction == "down":
        return "up"

def electrify_cell(cell):
    """Returns electrified image for a given image or None if this image has no electrified state"""
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
        edgePointingFromUpRight: electrifiedEdgePointingFromUpRight,
        inverter: electrifiedInverter
    }

    if not electrifiedImage.__contains__(cell.image):
        return []

    return [AffectedCell(cell.x, cell.y, electrifiedImage[cell.image])]

def deelectrify_cell(electrifiedCell):
    """Returns regular image for a given electrified image or None if this image has no regular state"""
    image = {
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
        electrifiedEdgePointingFromUpRight: edgePointingFromUpRight,
        electrifiedInverter: inverter
    }

    if not image.__contains__(electrifiedCell.image):
        return []

    return [AffectedCell(electrifiedCell.x, electrifiedCell.y, image[electrifiedCell.image])]

def check_cell_for_getting_connections(cell):
    connections = []

    if one_left_from(cell) != None and one_left_from(cell).image.gets == "right":
        connections += [one_left_from(cell)]
    if one_right_from(cell) != None and one_right_from(cell).image.gets == "left":
        connections += [one_right_from(cell)]
    if one_up_from(cell) != None and one_up_from(cell).image.gets == "down":
        connections += [one_up_from(cell)]
    if one_down_from(cell) != None and one_down_from(cell).image.gets == "up":
        connections += [one_down_from(cell)]
    return connections

def check_cell_for_giving_connections(cell):
    connections = []

    if one_left_from(cell) != None and one_left_from(cell).image.gives == "right":
        connections += [one_left_from(cell)]
    if one_right_from(cell) != None and one_right_from(cell).image.gives == "left":
        connections += [one_right_from(cell)]
    if one_up_from(cell) != None and one_up_from(cell).image.gives == "down":
        connections += [one_up_from(cell)]
    if one_down_from(cell) != None and one_down_from(cell).image.gives == "up":
        connections += [one_down_from(cell)]
    
    return connections

def generator_behaviour(current_cell):
    affected_cells = []

    for connection in check_cell_for_getting_connections(current_cell):
        affected_cells += electrify_cell(connection)

    return affected_cells

def electrified_arrow_behaviour(current_cell):
    affected_cells = []

    if current_cell.image.deleted == True:
        return []

    if one_front_from(current_cell) != None and one_front_from(current_cell).image.gets == invert_direction(current_cell.image.gives):
        affected_cells += electrify_cell(one_front_from(current_cell))

    if one_back_from(current_cell) != None and one_back_from(current_cell).image not in electrified_cells:
        affected_cells += deelectrify_cell(current_cell)
        
    return affected_cells

def inverter_behaviour(current_cell):
    affected_cells = []

    if current_cell.image.deleted == True:
        return []

    for connection in check_cell_for_giving_connections(current_cell):
        if connection.image.name in [element.name for element in electrified_arrows]:
            return affected_cells
        else:
            affected_cells += electrify_cell(current_cell)
            return affected_cells
            
    affected_cells += electrify_cell(current_cell)
    return affected_cells

def electrified_inverter_behaviour(current_cell):
    affected_cells = []

    if current_cell.image.deleted == True:
        return []

    for connection in check_cell_for_getting_connections(current_cell):
        affected_cells += electrify_cell(connection)
    
    for connection in check_cell_for_giving_connections(current_cell):
        if connection.image.name in [element.name for element in electrified_arrows]:
            affected_cells += deelectrify_cell(current_cell)
            break
    
    return affected_cells

def empty_conveyor_behaviour(current_cell):
    affected_cells = []
    
    if one_back_from(current_cell) != None and one_back_from(current_cell).image.name != "EmptyCell" and one_back_from(current_cell).image not in conveyors_containing_cells:
        affected_cells += [AffectedCell(current_cell.x, current_cell.y, eval(lower_first_letter(current_cell.image.name + "Containing" + one_back_from(current_cell).image.name)))]
        affected_cells += [AffectedCell(one_back_from(current_cell).x, one_back_from(current_cell).y, emptyCell)]
        one_back_from(current_cell).image.deleted = True

    return affected_cells

def conveyor_containing_cell_behaviour(current_cell):
    affected_cells = []

    if one_front_from(current_cell) != None:
        affected_cells += [AffectedCell(one_front_from(current_cell).x, one_front_from(current_cell).y, eval(lower_first_letter(current_cell.image.name.split("Containing")[1])))]
        affected_cells += [AffectedCell(current_cell.x, current_cell.y, eval(lower_first_letter(current_cell.image.name.split("Containing")[0])))]

    return affected_cells

def logic():
    affected_cells = []

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            cell = CellAt(x,y)
            cell.image.deleted = False

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            cell = CellAt(x,y)
            if cell.image in empty_conveyors:
                affected_cells += empty_conveyor_behaviour(cell)
            if cell.image in conveyors_containing_cells:
                affected_cells += conveyor_containing_cell_behaviour(cell)
            if cell.image == generator:
                affected_cells += generator_behaviour(cell)
            if cell.image in electrified_arrows:
                affected_cells += electrified_arrow_behaviour(cell)
            if cell.image == electrifiedInverter:
                affected_cells += electrified_inverter_behaviour(cell)
            if cell.image == inverter:
                affected_cells += inverter_behaviour(cell)

    for cell in affected_cells:
        set_cell(grid, cell.x, cell.y, cell.image)

def buttons_reaction(event):
    """ Handles a mouse click in the grid (per cell)"""
    if event.widget != CANVAS:
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