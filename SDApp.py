from SDButtons import SDButtons
from SDGUI import SDGUI

def main():
    buttons = SDButtons(init=False, SDName="SchoolDB.csv")
    gui = SDGUI(SDData=buttons)
    gui.mainloop()

if __name__ == "__main__":
    main()