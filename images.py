from tkinter import *

class Cell(PhotoImage):
    def __init__(self, gets, brings, name, file):
        PhotoImage.__init__(self, file=file, name=name)
        self.gets = gets
        self.brings = brings

tk = Tk()

#ICON
appIcon = PhotoImage(file="resources/arrow_circuits_icon.ico")

#CELLS
emptyCell = Cell(gets = None, brings = None, name="Eraser", file="resources/empty_cell.png")
generator = Cell(gets = None, brings = None, name="Create generator", file="resources/generator.png")

arrowPointingUp = Cell(gets = "down", brings = "up", name ="Arrow", file="resources/arrow_pUP.png")
arrowPointingDown = Cell(gets = "up", brings = "down", name ="a_d", file="resources/arrow_pDOWN.png")
arrowPointingLeft = Cell(gets = "right", brings = "left", name ="a_l", file="resources/arrow_pLEFT.png")
arrowPointingRight = Cell(gets = "left", brings = "right", name ="a_r", file="resources/arrow_pRIGHT.png")
electrifiedArrowPointingUp = Cell(gets = "down", brings = "up", name = "ea_u", file="resources/electrified_arrow_pUP.png")
electrifiedArrowPointingDown = Cell(gets = "up", brings = "down", name = "ea_d", file="resources/electrified_arrow_pDOWN.png")
electrifiedArrowPointingLeft = Cell(gets = "right", brings = "left", name = "ea_l", file="resources/electrified_arrow_pLEFT.png")
electrifiedArrowPointingRight = Cell(gets = "left", brings = "right", name = "ea_r", file="resources/electrified_arrow_pRIGHT.png")

edgePointingFromDownLeft = Cell(gets = "down", brings = "left", name = "e_fd_pl", file="resources/edge_fDOWN_pLEFT.png")
edgePointingFromDownRight = Cell(gets = "down", brings = "right", name = "e_fd_pr", file="resources/edge_fDOWN_pRIGHT.png")
edgePointingFromLeftDown = Cell(gets = "left", brings = "down", name = "e_fl_pd", file="resources/edge_fLEFT_pDOWN.png")
edgePointingFromLeftUp = Cell(gets = "left", brings = "up", name = "Edge", file="resources/edge_fLEFT_pUP.png")
edgePointingFromRightDown = Cell(gets = "right", brings = "down", name = "e_fr_pd", file="resources/edge_fRIGHT_pDOWN.png")
edgePointingFromRightUp = Cell(gets = "right", brings = "up", name = "e_fr_pu", file="resources/edge_fRIGHT_pUP.png")
edgePointingFromUpLeft = Cell(gets = "up", brings = "left", name = "e_fu_pl", file="resources/edge_fUP_pLEFT.png")
edgePointingFromUpRight = Cell(gets = "up", brings = "right", name = "e_fu_pr", file="resources/edge_fUP_pRIGHT.png")
electrifiedEdgePointingFromDownLeft = Cell(gets = "down", brings = "left", name = "ee_fd_pl", file="resources/electrified_edge_fDOWN_pLEFT.png")
electrifiedEdgePointingFromDownRight = Cell(gets = "down", brings = "right", name = "ee_fd_pr", file="resources/electrified_edge_fDOWN_pRIGHT.png")
electrifiedEdgePointingFromLeftDown = Cell(gets = "left", brings = "down", name = "ee_fl_pd", file="resources/electrified_edge_fLEFT_pDOWN.png")
electrifiedEdgePointingFromLeftUp = Cell(gets = "left", brings = "up", name = "ee_fl_pu", file="resources/electrified_edge_fLEFT_pUP.png")
electrifiedEdgePointingFromRightDown = Cell(gets = "right", brings = "down", name = "ee_fr_pd", file="resources/electrified_edge_fRIGHT_pDOWN.png")
electrifiedEdgePointingFromRightUp = Cell(gets = "right", brings = "up", name = "ee_fr_pu", file="resources/electrified_edge_fRIGHT_pUP.png")
electrifiedEdgePointingFromUpLeft = Cell(gets = "up", brings = "left", name = "ee_fu_pl", file="resources/electrified_edge_fUP_pLEFT.png")
electrifiedEdgePointingFromUpRight = Cell(gets = "up", brings = "right", name = "ee_fu_pr", file="resources/electrified_edge_fUP_pRIGHT.png")

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
                     generator]

#MENU ICONS
menuIconArrow = PhotoImage(file="resources/arrow_menu_icon.png")
menuIconCreateGenerator = PhotoImage(file="resources/create_generator_menu_icon.png")
menuIconEraser = PhotoImage(file="resources/eraser_menu_icon.png")
menuIconRotator = PhotoImage(file="resources/rotator_menu_icon.png")
menuIconEdge = PhotoImage(file="resources/edge_menu_icon.png")