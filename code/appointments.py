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

        global entry_image_1, entry_image_2, entry_image_3, entry_image_4, image_image_1
        global button_image_1, button_image_2
        entry_image_1 = PhotoImage(file=relative_to_assets("appointments/entry_1.png"))
        entry_image_2 = PhotoImage(file=relative_to_assets("appointments/entry_2.png"))
        entry_image_3 = PhotoImage(file=relative_to_assets("appointments/entry_3.png"))
        entry_image_4 = PhotoImage(file=relative_to_assets("appointments/entry_4.png"))
        image_image_1 = PhotoImage(file=relative_to_assets("appointments/image_1.png"))
        button_image_1 = PhotoImage(file=relative_to_assets("appointments/button_1.png"))
        button_image_2 = PhotoImage(file=relative_to_assets("appointments/button_2.png"))

        canvas.create_rectangle(
            0.0,
            0.0,
            49.0,
            600.0,
            fill="#F8CD8C",
            outline="")

        canvas.create_text(
            60.0,
            49.0,
            anchor="nw",
            text="Hey John!",
            fill="#000000",
            font=("Roboto", 20 * -1)
        )

        canvas.create_text(
            60.0,
            97.0,
            anchor="nw",
            text="Never miss out on your health!",
            fill="#000000",
            font=("Roboto", 20 * -1)
        )

        canvas.create_text(
            90.0,
            446.0,
            anchor="nw",
            text="For whom?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

        
        entry_bg_1 = canvas.create_image(
            212.0,
            497.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_1.place(
            x=99.0,
            y=485,
            width=225,
            height=25
        )

        canvas.create_text(
            90.0,
            172.0,
            anchor="nw",
            text="Whom are you consulting?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

        
        entry_bg_2 = canvas.create_image(
            205.0,
            223.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_2.place(
            x=92.0,
            y=210,
            width=225,
            height=25
        )

        canvas.create_text(
            90.0,
            264.0,
            anchor="nw",
            text="When?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

        
        entry_bg_3 = canvas.create_image(
            208.0,
            314.0,
            image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_3.place(
            x=95.0,
            y=301,
            width=225,
            height=25
        )

        canvas.create_text(
            90.0,
            355.0,
            anchor="nw",
            text="Where?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

        
        entry_bg_4 = canvas.create_image(
            212.0,
            405.0,
            image=entry_image_4
        )
        entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_4.place(
            x=99.0,
            y=393,
            width=225,
            height=25
        )

        
        image_1 = canvas.create_image(
            641.0,
            328.0,
            image=image_image_1
        )

        canvas.create_rectangle(
            642.0,
            32.0,
            875.0,
            81.0,
            fill="#FEECD0",
            outline="")

        canvas.create_text(
            667.0,
            46.0,
            anchor="nw",
            text="Appointments\n",
            fill="#000000",
            font=("Roboto", 16 * -1)
        )

        
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=541.0,
            y=512.0,
            width=202.77001953125,
            height=50.0
        )

        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=13.0,
            y=530.0,
            width=23.0,
            height=23.0
        )