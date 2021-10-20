from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame, Entry

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Appointments(Frame):
    def __init__(self, window, parent):
        Frame.__init__(self, parent)
        self.window = window

        canvas = Canvas(
            parent,
            bg = "#FFFFFF",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)

        global entryImage, image1
        global addNow, home
        entryImage = PhotoImage(file=relative_to_assets("appointments/entryimage.png"))
        image1 = PhotoImage(file=relative_to_assets("appointments/image_1.png"))
        addNow = PhotoImage(file=relative_to_assets("appointments/addNow.png"))
        home = PhotoImage(file=relative_to_assets("appointments/home.png"))

        canvas.create_rectangle(
            0,
            0,
            49,
            600,
            fill="#F8CD8C",
            outline="")

        canvas.create_text(
            60,
            49,
            anchor="nw",
            text="Hey John!",
            fill="#000000",
            font=("Roboto", 20 * -1)
        )
        canvas.create_text(
            60,
            97,
            anchor="nw",
            text="Never miss out on your health!",
            fill="#000000",
            font=("Roboto", 20 * -1)
        )

        canvas.create_text(
            90,
            446,
            anchor="nw",
            text="For whom?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )
        canvas.create_image(
            212,
            497,
            image=entryImage
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_1.place(
            x=99,
            y=485,
            width=225,
            height=25
        )
        canvas.create_text(
            90,
            172,
            anchor="nw",
            text="Whom are you consulting?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )
        canvas.create_image(
            205,
            223,
            image=entryImage
        )
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_2.place(
            x=92,
            y=210,
            width=225,
            height=25
        )
        canvas.create_text(
            90,
            264,
            anchor="nw",
            text="When?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )
        canvas.create_image(
            208,
            314,
            image=entryImage
        )
        entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_3.place(
            x=95,
            y=301,
            width=225,
            height=25
        )
        canvas.create_text(
            90,
            355,
            anchor="nw",
            text="Where?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )
        canvas.create_image(
            212,
            405,
            image=entryImage
        )
        entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_4.place(
            x=99,
            y=393,
            width=225,
            height=25
        )
        canvas.create_image(
            641,
            328,
            image=image1
        )

        canvas.create_rectangle(
            642,
            32,
            875,
            81,
            fill="#FEECD0",
            outline="")

        canvas.create_text(
            667,
            46,
            anchor="nw",
            text="Appointments\n",
            fill="#000000",
            font=("Roboto", 16 * -1)
        )

        
        btn_addNow = Button(
            image=addNow,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        btn_addNow.place(
            x=541,
            y=512,
            width=202.77001953125,
            height=50
        )

        btn_home = Button(
            image=home,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        btn_home.place(
            x=13,
            y=530,
            width=23,
            height=23
        )