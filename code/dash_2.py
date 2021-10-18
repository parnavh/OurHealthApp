from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Dash_2(Frame):
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

        global button_image_1, button_image_2, button_image_3, button_image_4
        global image_image_1, image_image_2
        button_image_1 = PhotoImage(file=relative_to_assets("2/button_1.png"))
        button_image_2 = PhotoImage(file=relative_to_assets("2/button_2.png"))
        button_image_3 = PhotoImage(file=relative_to_assets("2/button_3.png"))
        button_image_4 = PhotoImage(file=relative_to_assets("2/button_4.png"))
        image_image_1 = PhotoImage(file=relative_to_assets("2/image_1.png"))
        image_image_2 = PhotoImage(file=relative_to_assets("2/image_2.png"))

        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=195.0,
            y=176.0,
            width=94.0,
            height=33.0
        )

        
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=583.0,
            y=174.0,
            width=115.0,
            height=35.0
        )

        
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=363.0,
            y=175.0,
            width=134.0,
            height=34.0
        )

        canvas.create_rectangle(
            49.0,
            209.0,
            800.0,
            600.0,
            fill="#F8F7F2",
            outline="")

        canvas.create_rectangle(
            369.0,
            209.0,
            489.0,
            209.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_rectangle(
            0.0,
            0.0,
            49.0,
            600.0,
            fill="#F8CD8C",
            outline="")

        canvas.create_text(
            123.6046142578125,
            53.838714599609375,
            anchor="nw",
            text="JOHN DOE",
            fill="#000000",
            font=("Roboto", 20 * -1)
        )

        canvas.create_text(
            123.632080078125,
            83.10525512695312,
            anchor="nw",
            text="AGE: 18",
            fill="#000000",
            font=("Roboto", 16 * -1)
        )

        
        image_1 = canvas.create_image(
            91.0,
            79.0,
            image=image_image_1
        )

        canvas.create_rectangle(
            77.97000122070312,
            244.0,
            761.3800354003906,
            284.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_text(
            156.28997802734375,
            250.0,
            anchor="nw",
            text="Appointment with Dr. John Doe",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

        canvas.create_text(
            156.28997802734375,
            266.0,
            anchor="nw",
            text="Time: 2:00 P.M IST,",
            fill="#000000",
            font=("Roboto", 12 * -1)
        )

        
        image_2 = canvas.create_image(
            104.0,
            266.0,
            image=image_image_2
        )

        
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=324.0,
            y=521.0,
            width=202.77001953125,
            height=50.0
        )