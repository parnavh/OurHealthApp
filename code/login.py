from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame, Entry

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/login")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class login(Frame):
    def __init__(self, window, parent):
        Frame.__init__(self, parent)
        self.window = window
        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)

        global image_image_1, image_image_2, image_image_3, button_image_1, entry_image_1, entry_image_2
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        
        canvas.create_image(
            180,
            70,
            image=image_image_1
        )
        canvas.create_text(
            80.0,
            185.0,
            anchor="nw",
            text="Access your account!",
            fill="#000000",
            font=("Roboto", 18 * -1)
        )
        canvas.create_image(
            194.0,
            275.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_1.place(
            x=82.0,
            y=259.0,
            width=224.0,
            height=28.0
        )

        canvas.create_text(
            84.0,
            235.0,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Roboto", 12 * -1)
        )

        canvas.create_image(
            194.0,
            340.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            show='*'
        )
        entry_2.place(
            x=82.0,
            y=324.0,
            width=224.0,
            height=28.0
        )

        canvas.create_text(
            84.0,
            303.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Roboto", 12 * -1)
        )
        canvas.create_image(
            603.0,
            300.0,
            image=image_image_2
        )
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=70.0,
            y=388.0,
            width=242,
            height=36.0
        )
        canvas.create_image(
            580.0,
            458.0,
            image=image_image_3
        )