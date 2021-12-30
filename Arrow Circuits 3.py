from tkinter import *
import pyautogui as guy

tk = Tk()
tk['bg'] = '#ffffff'
tk.title('Arrow Circuits')

emptyCell = PhotoImage(name="Eraser", file="resources/empty_cell.png")
electrifiedEmptyCell = PhotoImage(name="Electrify", file="resources/electrified_empty_cell.png")
arrowPointingUp = PhotoImage(name="Arrow", file="resources/arrow_pUP.png")
arrowPointingDown = PhotoImage(file="resources/arrow_pDOWN.png")
arrowPointingLeft = PhotoImage(file="resources/arrow_pLEFT.png")
arrowPointingRight = PhotoImage(file="resources/arrow_pRIGHT.png")
electrifiedArrowPointingUp = PhotoImage(file="resources/electrified_arrow_pUP.png")
electrifiedArrowPointingDown = PhotoImage(file="resources/electrified_arrow_pDOWN.png")
electrifiedArrowPointingLeft = PhotoImage(file="resources/electrified_arrow_pLEFT.png")
electrifiedArrowPointingRight = PhotoImage(file="resources/electrified_arrow_pRIGHT.png")

menuIconArrow = PhotoImage(file="resources/arrow_menu_icon.png")
menuIconElectrify = PhotoImage(file="resources/electrify_menu_icon.png")
menuIconEraser = PhotoImage(file="resources/eraser_menu_icon.png")
menuIconRotate = PhotoImage(file="resources/rotate_menu_icon.png")

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
grid = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

for i in range (0, int((window_height - img_height * 3) / 57), 1):
    for j in range(0, window_width, img_width):
        grid[i].append(emptyCell)

def draw_image(imgNumber, image):
    canvas.create_image(imgNumber[0] * img_width, imgNumber[1] * img_height, anchor = NW, image = image)

def get_img_number(x, y):
    return (int(x / img_width), int(y / img_height))

def draw_grid(grid):
    for iy in range (0, len(grid)):
        for ix in range(0, len(grid[iy])):
            draw_image((ix, iy), grid[iy][ix])

def set_cell(grid, x, y, image):
    grid[y][x] = image
    draw_image((x,y), image)

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
        images = [arrowPointingUp, arrowPointingRight, arrowPointingDown, arrowPointingLeft]
        current_cell_image = grid[y][x]
        try:
            next_image = images[(images.index(current_cell_image) + 1) % len(images)]
        except ValueError:
            return
        set_cell(grid, x, y, next_image)
    rotator_tool.name = "Rotator"
    return rotator_tool

menuButtonEraser = Button(tk, image = menuIconEraser, command = lambda: select_tool(make_image_tool(emptyCell)))
menuButtonEraser.place(x=50, y= img_height * 15.5)

menuButtonElectrify = Button(tk, image = menuIconElectrify, command = lambda: select_tool(make_image_tool(electrifiedEmptyCell)))
menuButtonElectrify.place(x=214, y= img_height * 15.5)

menuButtonRotate = Button(tk, image = menuIconRotate, command = lambda: select_tool(make_rotator_tool()))
menuButtonRotate.place(x=378, y= img_height * 15.5)

menuButtonArrow = Button(tk, image = menuIconArrow, command = lambda: select_tool(make_image_tool(arrowPointingUp)))
menuButtonArrow.place(x=542, y= img_height * 15.5)
    
def buttons_reaction(event):
    if event.widget != canvas:
        return

    (x, y) = get_img_number(event.x, event.y)
    current_tool(x, y)

tk.bind('<Button-1>', buttons_reaction)
tk.bind('<B1-Motion>', buttons_reaction)

tk.mainloop()