from tkinter import *
import pyautogui as guy

tk = Tk()
tk['bg'] = '#ffffff'
tk.title('Arrow Circuits')

emptyCell = PhotoImage(name="Empty cell", file="resources/empty_cell.png")
electrifiedEmptyCell = PhotoImage(name="Electrify", file="resources/electrified_empty_cell.png")
arrowPointingUp = PhotoImage("Arrow", file="resources/arrow_pUP.png")
arrowPointingDown = PhotoImage(file="resources/arrow_pDOWN.png")
arrowPointingLeft = PhotoImage(file="resources/arrow_pLEFT.png")
arrowPointingRight = PhotoImage(file="resources/arrow_pRIGHT.png")
electrifiedArrowPointingUp = PhotoImage(file="resources/electrified_arrow_pUP.png")
electrifiedArrowPointingDown = PhotoImage(file="resources/electrified_arrow_pDOWN.png")
electrifiedArrowPointingLeft = PhotoImage(file="resources/electrified_arrow_pLEFT.png")
electrifiedArrowPointingRight = PhotoImage(file="resources/electrified_arrow_pRIGHT.png")
menuIconArrow = PhotoImage(file="resources/arrow_menu_icon.png")
menuIconElectrify = PhotoImage(file="resources/electrify_menu_icon.png")

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
grid = ()

for y in range (0, window_height - img_height * 3, img_height):
    for x in range(0, window_width, img_width):
        canvas.create_image(x, y, anchor = NW, image = emptyCell)

#MENU
def select_tool(tool):
    global selected_image
    selected_image = tool
    print("[LOG]: selected tool: " + tool.name)

menuButtonElectrify = Button(tk, image = menuIconElectrify, command = lambda: select_tool(electrifiedEmptyCell))
menuButtonElectrify.place(x=50, y= img_height * 15.5)

menuButtonArrow = Button(tk, image = menuIconArrow, command = lambda: select_tool(arrowPointingUp))
menuButtonArrow.place(x=214, y= img_height * 15.5)

def draw_image(imgNumber, image):
    canvas.create_image(imgNumber[0] * img_width, imgNumber[1] * img_height, anchor = NW, image = image)

def change_image(imgNumber, image):
    draw_image(imgNumber, image)
    
def fix_image(event):
    if event.widget != canvas:
        return
    imgNumber = (int(event.x / img_width), int(event.y / img_height))
    if imgNumber[0] < 33 and imgNumber[1] < 15:
        draw_image(imgNumber, selected_image)

tk.bind('<Button-1>', fix_image)

#tk.mainloop()
