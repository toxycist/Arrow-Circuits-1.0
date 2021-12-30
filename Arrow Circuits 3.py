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

selected_image = emptyCell

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

draw_grid(grid)
#MENU
def select_tool(tool):
    global selected_image
    selected_image = tool
    print("Selected tool: " + tool.name)

menuButtonElectrify = Button(tk, image = menuIconElectrify, command = lambda: select_tool(electrifiedEmptyCell))
menuButtonElectrify.place(x=50, y= img_height * 15.5)

menuButtonArrow = Button(tk, image = menuIconArrow, command = lambda: select_tool(arrowPointingUp))
menuButtonArrow.place(x=214, y= img_height * 15.5)

menuButtonEraser = Button(tk, image = menuIconEraser, command = lambda: select_tool(emptyCell))
menuButtonEraser.place(x=378, y= img_height * 15.5)

def change_image(imgNumber, image):
    draw_image(imgNumber, image)
    
def fix_image(event):
    if event.widget != canvas:
        return
    imgNumber = get_img_number(event.x, event.y)
    if imgNumber[0] < 33 and imgNumber[1] < 15:
        draw_image(imgNumber, selected_image)

tk.bind('<B1-Motion>', fix_image)

tk.mainloop()
